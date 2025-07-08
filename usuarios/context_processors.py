# context_processors.py (versão atualizada)
from django.utils import timezone
from django.core.cache import cache
from django.conf import settings
from openai import OpenAI
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)

def openai_balance(request):
    try:
        # Verifica se a chave está configurada
        if not getattr(settings, 'OPENAI_API_KEY', None):
            # logger.error("OPENAI_API_KEY não encontrada nas configurações")
            return {'openai_balance': None}
            
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        
        # Tenta obter do cache primeiro
        balance = cache.get('openai_balance')
        if balance:
            return {'openai_balance': balance}
            
        # Chamada real à API
        usage = client.usage.retrieve()
        logger.debug(f"Resposta da API: {usage}")
        
        # Cálculos
        used = Decimal(usage.total_usage) / 100  # Convertendo centavos para dólares
        limit = Decimal(str(settings.OPENAI_MONTHLY_LIMIT))
        remaining = limit - used
        
        # Montagem dos dados
        balance_data = {
            'dollars': remaining,
            'tokens': (remaining / Decimal('0.002')) * 1000,  # Taxa do GPT-3.5 Turbo
            'last_updated': timezone.now()
        }
        
        # Atualiza cache por 5 minutos
        cache.set('openai_balance', balance_data, 300)
        
        return {'openai_balance': balance_data}
        
    except Exception as e:
        logger.error(f"Erro ao obter saldo OpenAI: {str(e)}")
        return {'openai_balance': None}