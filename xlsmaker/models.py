from django.db import models
from django.contrib.auth.models import User
import re
import ast
from functools import lru_cache
import difflib
class Solicitacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)    
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    descricao = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True , null=True, blank=True)  

def __str__(self):
    return self.model  

class Meta:
        ordering = ['-created_at']  # Ordena do mais recente para o mais antigo
        

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True)
#     tokens_atribuidos = models.IntegerField(default=1000)
#     tokens_gastos = models.IntegerField(default=0)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True)
    tokens_atribuidos = models.IntegerField(default=10000)
    tokens_gastos = models.IntegerField(default=0)

    @property
    def saldo_tokens(self):
        return self.tokens_atribuidos - self.tokens_gastos



class FormulaIntelligence:
    def __init__(self):
        self.excel_functions = {     
                "Inglês": {                   
                    "DATA":"DATE", 
                    "CONCATENAR":"CONCAT",
                    "ABS": "ABS",
                    "ENDEREÇO": "ADDRESS",
                    "AGREGAR": "AGGREGATE",         
                    "ÉERROS": "ISERROR",           
                    
                    # Lógicas
                    "E": "AND",
                    "OU": "OR",
                    "SE": "IF",
                    "FALSO": "FALSE",
                    "VERDADEIRO": "TRUE",
                    "ÉERROS": "ISERROR",
                    "ÉCÉL.VAZIA": "ISBLANK",
                    
                    # Matemáticas
                    "PAR": "EVEN",
                    "ÍMPAR": "ODD",
                    "FATORIAL": "FACT",
                    "FATDUPLO": "FACTDOUBLE",
                    "PI": "PI",
                    "ARRED": "ROUND",
                    "TETO": "CEILING",
                    "PISO": "FLOOR",
                    "MODO": "MODE",
                    
                    # Estatísticas
                    "CONTAR": "COUNT",
                    "CONT.VALORES": "COUNTA",
                    "CONTAR.VAZIO": "COUNTBLANK",
                    "CONT.SE": "COUNTIF",
                    "CONT.SES": "COUNTIFS",
                    "MÉDIA": "AVERAGE",
                    "MÉDIASE": "AVERAGEIF",
                    "MÁXIMO": "MAX",
                    "MÍNIMO": "MIN",  
                    "SOMA": "SUM",          
                    "SOMASE": "SUMIF",   
                    "SOMASES": "SUMIFS",        
                                
                    # Texto
                    "EXACTO": "EXACT",
                    "MINÚSCULA": "LOWER",
                    "MAIÚSCULA": "UPPER",
                    "PRI.MAIÚSCULA": "PROPER",
                    "EXT.TEXTO": "MID",
                    
                    # Data
                    "HOJE": "TODAY",
                    "AGORA": "NOW",
                    "DIA": "DAY",
                    "MÊS": "MONTH",
                    "ANO": "YEAR",
                    
                    # Procura
                    "PROCV": "VLOOKUP",
                    "PROCH": "HLOOKUP",
                    "ÍNDICE": "INDEX",
                    "CORRESP": "MATCH"
                   
                },
                "Português": {
                   
                    "DATE":"DATA",
                    "CONCAT":"CONCATENAR",
                    "ABS": "ABS",
                    "ADDRESS": "ENDEREÇO",
                    "AGGREGATE": "AGREGAR",          
                    "ISERROR": "ÉERROS",            
                    
                    # Lógicas
                    "AND": "E",
                    "OR": "OU",
                    "IF": "SE",
                    "FALSE": "FALSO",
                    "TRUE": "VERDADEIRO",
                    "ISERROR": "ÉERROS",
                    "ISBLANK": "ÉCÉL.VAZIA",
                    
                    # Matemáticas
                    "EVEN": "PAR",
                    "ODD": "ÍMPAR",
                    "FACT": "FATORIAL",
                    "FACTDOUBLE": "FATDUPLO",
                    "PI": "PI",
                    "ROUND": "ARRED",
                    "CEILING": "TETO",
                    "FLOOR": "PISO",
                    "MODE": "MODO",
                     
                    # Estatísticas
                    "COUNT": "CONTAR",
                    "COUNTA": "CONT.VALORES",
                    "COUNTBLANK": "CONTAR.VAZIO",
                    "COUNTIF": "CONT.SE",
                    "COUNTIFS": "CONT.SES",
                    "AVERAGE": "MÉDIA",           
                    "AVERAGEIF": "MÉDIASE",
                    "MAX": "MÁXIMO",
                    "MIN": "MÍNIMO",
                    "SUM": "SOMA",
                    "SUMIF": "SOMASE", 
                    "SUMIFS": "SOMASES",                        
                                
                    # Texto
                    "EXACT": "EXACTO",
                    "LOWER": "MINÚSCULA",
                    "UPPER": "MAIÚSCULA",
                    "PROPER": "PRI.MAIÚSCULA",
                    "MID": "EXT.TEXTO",
                                
                    # Data
                    "TODAY": "HOJE",
                    "NOW": "AGORA",
                    "DAY": "DIA",
                    "MONTH": "MÊS",
                    "YEAR": "ANO",
                    
                    # Procura
                    "VLOOKUP": "PROCV",
                    "HLOOKUP": "PROCH",
                    "INDEX": "ÍNDICE",
                    "MATCH": "CORRESP"
                    }
        }
        
        self.translations = {
            "pt": {
                # "PROCV": "VLOOKUP",
                # "PROCH": "HLOOKUP",
                # "SE": "IF",
                # "E": "AND",
                # "OU": "OR",
                # "FALSO": "FALSE",
                # "VERDADEIRO": "TRUE",                
                
                "DATA":"DATE",
                "CONCATENAR":"CONCAT",
                "ABS": "ABS",
                "ENDEREÇO": "ADDRESS",
                "AGREGAR": "AGGREGATE",          
                "ÉERROS": "ISERROR",            
                
                # Lógicas
                "E": "AND",
                "OU": "OR",
                "SE": "IF",
                "FALSO": "FALSE",
                "VERDADEIRO": "TRUE",
                "ÉCÉL.VAZIA": "ISBLANK",
                
                # Matemáticas
                "PAR": "EVEN",
                "ÍMPAR": "ODD",
                "FATORIAL": "FACT",
                "FATDUPLO": "FACTDOUBLE",
                "PI": "PI",
                "ARRED": "ROUND",
                "TETO": "CEILING",
                "PISO": "FLOOR",
                "MODO": "MODE",
                    
                # Estatísticas
                "CONTAR":"COUNT",
                "CONT.VALORES":"COUNTA",
                "CONTAR.VAZIO":"COUNTBLANK",
                "CONT.SE":"COUNTIF",
                "CONT.SES":"COUNTIFS",
                "MÉDIA":"AVERAGE",           
                "MÉDIASE":"AVERAGEIF",
                "MÁXIMO":"MAX",
                "MÍNIMO":"MIN",
                "SOMA":"SUM",
                "SOMASE":"SUMIF", 
                "SOMASES":"SUMIFS",                        
                            
                # Texto
                "EXACTO":"EXACT",
                "MINÚSCULA":"LOWER",
                "MAIÚSCULA":"UPPER",
                "PRI.MAIÚSCULA":"PROPER",
                "EXT.TEXTO":"MID",
                            
                # Data
                "HOJE":"TODAY",
                "AGORA":"NOW",
                "DIA":"DAY",
                "MÊS":"MONTH",
                "ANO":"YEAR",
                
                # Procura
                "PROCV":"VLOOKUP",
                "PROCH":"HLOOKUP",
                "ÍNDICE":"INDEX",
                "CORRESP":"MATCH",
            },
            "en": {
                # "VLOOKUP": "PROCV",
                # "HLOOKUP": "PROCH",
                # "IF": "SE",
                # "AND": "E",
                # "OR": "OU",
                # "FALSE": "FALSO",
                # "TRUE": "VERDADEIRO",
                                
                "DATE":"DATA",
                "CONCAT":"CONCATENAR",
                "ABS": "ABS",
                "ADDRESS": "ENDEREÇO",
                "AGGREGATE": "AGREGAR",          
                "ISERROR": "ÉERROS",            
                
                # Lógicas
                "AND": "E",
                "OR": "OU",
                "IF": "SE",
                "FALSE": "FALSO",
                "TRUE": "VERDADEIRO",
                "ISERROR": "ÉERROS",
                "ISBLANK": "ÉCÉL.VAZIA",
                
                # Matemáticas
                "EVEN": "PAR",
                "ODD": "ÍMPAR",
                "FACT": "FATORIAL",
                "FACTDOUBLE": "FATDUPLO",
                "PI": "PI",
                "ROUND": "ARRED",
                "CEILING": "TETO",
                "FLOOR": "PISO",
                "MODE": "MODO",
                    
                # Estatísticas
                "COUNT": "CONTAR",
                "COUNTA": "CONT.VALORES",
                "COUNTBLANK": "CONTAR.VAZIO",
                "COUNTIF": "CONT.SE",
                "COUNTIFS": "CONT.SES",
                "AVERAGE": "MÉDIA",           
                "AVERAGEIF": "MÉDIASE",
                "MAX": "MÁXIMO",
                "MIN": "MÍNIMO",
                "SUM": "SOMA",
                "SUMIF": "SOMASE", 
                "SUMIFS": "SOMASES",                        
                            
                # Texto
                "EXACT": "EXACTO",
                "LOWER": "MINÚSCULA",
                "UPPER": "MAIÚSCULA",
                "PROPER": "PRI.MAIÚSCULA",
                "MID": "EXT.TEXTO",
                            
                # Data
                "TODAY": "HOJE",
                "NOW": "AGORA",
                "DAY": "DIA",
                "MONTH": "MÊS",
                "YEAR": "ANO",
                
                # Procura
                "VLOOKUP": "PROCV",
                "HLOOKUP": "PROCH",
                "INDEX": "ÍNDICE",
                "MATCH": "CORRESP"
            },
        }
        self.function_map = self.load_function_mappings()
        self.syntax_validator = self.create_syntax_validator()
        self.abas_existentes = [] 

    def load_function_mappings(self):
        return {
            'Inglês': {
                **self.excel_functions['Inglês'],
                'reverse': {v: k for k, v in self.excel_functions['Português'].items()}
            },
            'Português': {
                **self.excel_functions['Português'],
                'reverse': {v: k for k, v in self.excel_functions['Inglês'].items()}
            }
        }

    def create_syntax_validator(self):
        return {
            'SUMIFS': (3, None),
            'SOMASES': (3, None),
            'VLOOKUP': (3, 4),
            'PROCV': (3, 4)
        }
    
        
    def clean_formula(self, formula: str) -> str:
        """
        Remove aspas problemáticas de fórmulas de forma segura, preservando:
        - Fórmulas simples (e.g., "=A1+B1")
        - Fórmulas complexas com aspas internas (e.g., "=SUMIF(A:A,\">10\")")
        """
        if not isinstance(formula, str):
            return formula
            
        # Remove todas as aspas externas (caso ="=formula")
        formula = formula.strip('"')
        
        # Se não começa com '=', não é fórmula - devolve sem processar
        if not formula.startswith('='):
            return formula
            
        # Caso especial: fórmulas simples entre aspas (="A1+B1")
        if re.match(r'^=[^\(\)]+$', formula):
            return formula
            
        # Preserva aspas internas necessárias (para critérios textuais)
        preserved = []
        def replace_quotes(match):
            preserved.append(match.group(0))
            return f'__TEMP_QUOTE_{len(preserved)-1}__'
        
        # Temporariamente substitui aspas internas
        temp_formula = re.sub(r'("[^"]+")', replace_quotes, formula)
        
        # Remove todas outras aspas
        temp_formula = temp_formula.replace('"', '')
        
        # Restaura aspas preservadas
        for i, quote in enumerate(preserved):
            temp_formula = temp_formula.replace(f'__TEMP_QUOTE_{i}__', quote)
        
        return temp_formula
   
    
    def translate_formulas(self, formula, language):
        try:
            formula = self.preprocess_formula(formula)
            
            # Verifica se já está no formato correto
            if re.match(r'^=[A-Z]+\s*\(', formula, re.IGNORECASE):
                syntax_tree = self.parse_formula(formula)
                translated = self.translate_node(syntax_tree, language)
            else:
                # Fallback para tradução direta
                if language == 'Português':
                    translated = self._translate_to_portuguese(formula)
                else:
                    translated = self._translate_to_english(formula)
            
            return self.postprocess_formula(translated, language)
        except Exception as e:
            print(f"Erro na tradução: {str(e)}")
            return formula
        
        
        
    def _translate_to_portuguese(self, formula):
        translations = self.excel_functions['Português']
        for eng, pt in translations.items():
            if eng != pt:
                formula = re.sub(rf'\b{eng}\b', pt, formula, flags=re.IGNORECASE)
        return formula

    def _translate_to_english(self, formula):
        translations = self.excel_functions['Inglês']
        for pt, eng in translations.items():
            if pt != eng:
                formula = re.sub(rf'\b{pt}\b', eng, formula, flags=re.IGNORECASE)
        return formula
        


    def preprocess_formula(self, formula):        
        # Corrige tanto MIN quanto MAX
        formula = re.sub(r'(?i)@MÍNIMO\b', 'MIN', formula)
        formula = re.sub(r'(?i)@MIN\b', 'MIN', formula)
        formula = re.sub(r'(?i)@MÁXIMO\b', 'MAX', formula)
        formula = re.sub(r'(?i)@MAX\b', 'MAX', formula)
        formula = re.sub(r'(?i)\b(TRUE|FALSE)\b', lambda m: m.group().upper(), formula)
        formula = re.sub(r'"\s*&\s*"', '', formula)
        return formula.replace('=@', '=').strip()

   
    def parse_formula(self, formula):
          # Agora aceita nomes com ponto
        pattern = r'^=([A-ZÇÁÉÍÓÚÂÊÔÃÕÜ\.]+)\((.*)\)$'
        match = re.match(pattern, formula.strip(), re.IGNORECASE)
        if not match:
            return {'type': 'string', 'value': formula}
    
        func_name = match.group(1).upper()
        args_str = match.group(2)
    
        args = self.split_arguments(args_str)
    
        parsed_args = []
        for arg in args:
            arg = arg.strip()
            if re.match(r'^-?\d+(\.\d+)?$', arg):  # número
                parsed_args.append({'type': 'number', 'value': float(arg) if '.' in arg else int(arg)})
            elif re.match(r'^[A-Z]+[0-9]+(:[A-Z]+[0-9]+)?$', arg, re.IGNORECASE):  # referência ou intervalo
                parsed_args.append({'type': 'reference', 'value': arg})
            elif re.match(r'^".*"$', arg):  # texto entre aspas
                parsed_args.append({'type': 'string', 'value': arg.strip('"')})
            elif re.match(r'^[A-ZÇÁÉÍÓÚÂÊÔÃÕÜ\.]+\(', arg, re.IGNORECASE):  # função aninhada com ponto
                parsed_args.append(self.parse_formula(f'={arg}'))
            else:
                parsed_args.append({'type': 'unknown', 'value': arg})

    
        return {
            'type': 'function',
            'name': func_name,
            'args': parsed_args
        }
    
    def split_arguments(self, args_str):
        args = []
        current = ''
        in_quotes = False
        depth = 0
        for char in args_str:
            if char == '"':
                in_quotes = not in_quotes
            elif char in ['(', ')'] and not in_quotes:
                depth += 1 if char == '(' else -1
            elif char in [';', ','] and not in_quotes and depth == 0:
                args.append(current)
                current = ''
                continue
            current += char
        if current:
            args.append(current)
        return args


    def analyze_ast(self, node):
        if isinstance(node, ast.Call):
            func_name = node.func.id.upper() if isinstance(node.func, ast.Name) else ''
            args = [self.analyze_ast(arg) for arg in node.args]
            return {'type': 'function', 'name': func_name, 'args': args}
        elif isinstance(node, ast.Str):
            return {'type': 'string', 'value': node.s}
        elif isinstance(node, ast.Num):
            return {'type': 'number', 'value': node.n}
        elif isinstance(node, ast.Name):
            return {'type': 'reference', 'value': node.id}
        elif isinstance(node, ast.BinOp):
            return {
                'type': 'operation',
                'left': self.analyze_ast(node.left),
                'op': type(node.op).__name__,
                'right': self.analyze_ast(node.right)
            }
        return str(node)



    def translate_node(self, node, language):
        if isinstance(node, dict):
            if node['type'] == 'function':
                return self.translate_function(node, language)
            elif node['type'] == 'string':
                return f'"{node["value"]}"'
            elif node['type'] == 'number':
                return str(node['value'])
            elif node['type'] == 'reference':
                return node['value']
            elif node['type'] == 'unknown':
                val = node['value'].upper()
                if val in ['TRUE', 'FALSE', 'VERDADEIRO', 'FALSO']:
                    return self.function_map[language].get(val, val)
                return val
        return str(node)


    def translate_function(self, node, language):
        original_name = node['name']
        translated_name = self.function_map[language].get(original_name, original_name)
        args = [self.translate_node(arg, language) for arg in node['args']]
        self.validate_function_syntax(translated_name, len(args))
        processed_args = [str(arg) for arg in args]
        return f"{translated_name}({self.join_arguments(processed_args, language)})"

    def validate_function_syntax(self, func_name, arg_count):
        rules = self.syntax_validator.get(func_name.upper())
        if rules:
            min_args, max_args = rules
            if (min_args and arg_count < min_args) or (max_args and arg_count > max_args):
                raise ValueError(f"Função {func_name} com número inválido de argumentos: {arg_count}")

    def join_arguments(self, args, language):
        separator = ',' if language == 'Inglês' else ';'
        return separator.join(args)

    def convert_reference(self, ref, language):
        if re.match(r'^[A-Z]+\d+$', ref):
            return ref
        return self.convert_style(ref, language)

    def convert_style(self, ref, language):
        return ref  # Placeholder (não implementado)

    
    def postprocess_formula(self, formula, language):
        # Aplica a limpeza de aspas primeiro
        formula = self.clean_formula(formula) 
        formula = self._fix_nested_min_max(formula)  # Novo tratamento       
        # Processamento original
        formula = self.fix_quotes(formula)
        formula = self.adjust_separators(formula, language)
        formula = self.fix_nested_functions(formula)
        
        # Garante que começa com '='
        if not formula.startswith('=') and any(c in formula for c in '+-*/^()'):
            formula = '=' + formula
            
        return formula
    
    

    def fix_quotes(self, formula):
        formula = re.sub(r'(?i)(\W)(entrada|sa[íi]da|crit[eé]rio)(\W)',lambda m: f'{m.group(1)}"{m.group(2).capitalize()}"{m.group(3)}', formula)
        return re.sub(r'""+', '"', formula)

    def adjust_separators(self, formula, language):
        target_sep = ',' if language == 'Inglês' else ';'
        opposite_sep = ';' if target_sep == ',' else ','
        return formula.replace(opposite_sep, target_sep)
    
    def _fix_nested_min_max(self, formula):
        # Corrige ambos MIN e MAX
        return re.sub(
            r'=IF\(([^=]+)=@?(MÍNIMO|MIN|MÁXIMO|MAX)\(([^)]+)\)',
            lambda m: f'=IF({m.group(1)}={m.group(2).upper()}({m.group(3)})',
            formula,
            flags=re.IGNORECASE
        )

    def fix_nested_functions(self, formula):
        return re.sub(r'([A-Z]+)\(([^)]+)\)',lambda m: f'{m.group(1)}({self.fix_inner_separators(m.group(2))})', formula)

    def fix_inner_separators(self, content):
        return re.sub(r',(?=[^"]*"(?:[^"]*"[^"]*")*[^"]*$)', ';', content)

    def fallback_parse(self, formula):
        return {'type': 'string', 'value': formula}
    
    def translate_function_name(self, name: str, target_language: str) -> str:
        if name.upper() in ('MIN', 'MAX', 'MÍNIMO', 'MÁXIMO'):
            if target_language == 'Inglês':
                return 'MIN' if name.upper() in ('MIN', 'MÍNIMO') else 'MAX'
            else:
                return 'MÍNIMO' if name.upper() in ('MIN', 'MÍNIMO') else 'MÁXIMO'
        mapping = self.translations["pt" if target_language == "Inglês" else "en"]
        return mapping.get(name.upper(), name.upper())

  
    def translate_logical_values(self, arg: str, target_language: str) -> str:
        mapping = self.translations["pt" if target_language == "Inglês" else "en"]
        upper_arg = arg.upper()
    
        # Tentar mapear erros comuns
        equivalencias = {
            "FALIF": "FALSO", "FALS": "FALSO", "FALSE": "FALSO", "FALSO": "FALSO", "FALIIF":"FALSO",
            "VERDADEIRO": "VERDADEIRO", "TRUE": "VERDADEIRO"
        } if target_language == "Português" else {
            "FALIF": "FALSE", "FALS": "FALSE", "FALSO": "FALSE", "FALSE": "FALSE", "FALIIF":"FALSE",
            "VERDADEIRO": "TRUE", "TRUE": "TRUE"
        }
    
        valor_corrigido = equivalencias.get(upper_arg, arg)
        return mapping.get(valor_corrigido, valor_corrigido)

    
    def _encontrar_coluna_relacionamento(self, colunas_planilha: list) -> str:
        """Identifica a coluna de relacionamento com inteligência contextual"""
        # 1. Busca por padrões explícitos primeiro
        padroes = [
            r'id_', r'cod', r'id\b', r'\bid\b', 
            r'chave', r'código', r'fk', r'ref', r'relaciona'
        ]
        
        for col in reversed(colunas_planilha):  # Verifica da direita para esquerda
            if any(re.search(padrao, col, re.IGNORECASE) for padrao in padroes):
                return col
        
        # 2. Fallback: procura a primeira coluna que parece ser ID (não descritiva)
        for col in colunas_planilha:
            if len(col) <= 8 and not any(palavra in col.lower() 
                                    for palavra in ['nome', 'descri', 'name', 'observa']):
                return col
        
        # 3. Último recurso: usa a última coluna antes da coluna atual (mais comum)
        return colunas_planilha[-1] if colunas_planilha else 'A'

        
    def _corrigir_referencia_vlookup(self, formula: str, colunas_planilha: list, language: str) -> str:
        """Corrige referências VLOOKUP/PROCV com base nas colunas disponíveis"""
        def replacer(match):
            func_name = match.group(1).upper()
            separator = ',' if language == 'Inglês' else ';'
            args = [arg.strip() for arg in re.split(r'[,;]', match.group(2))]
            
            if len(args) >= 3:
                # Encontra a melhor coluna para relacionamento
                col_rel = self._encontrar_coluna_relacionamento(colunas_planilha)
                if col_rel in colunas_planilha:
                    col_idx = colunas_planilha.index(col_rel)
                    
                    # Converte índice para letra de coluna (A, B, ..., AA, AB)
                    col_letter = ''
                    idx = col_idx
                    while idx >= 0:
                        col_letter = chr(65 + (idx % 26)) + col_letter
                        idx = idx // 26 - 1
                    
                    # Corrige a referência (ex: A2 → F2)
                    args[0] = re.sub(r'([A-Z]+)(\d+)', f'{col_letter}\\2', args[0])
                    
                    return f"{func_name}({separator.join(args)})"
                
            return match.group(0)
        
        # Aplica apenas a VLOOKUP/PROCV
        return re.sub(r'(VLOOKUP|PROCV)\(([^)]+)\)', replacer, formula, flags=re.IGNORECASE)
    
    
    
    
  
    def corrigir_formulas_comuns(self, formula: str, idioma='pt', abas_existentes=None, colunas_por_aba=None, nome_aba_atual=None) -> str:
        if not isinstance(formula, str) or not formula.startswith('='):
            return formula
        
        idioma = 'pt' if idioma.startswith('pt') else 'en'
        target_language = "Português" if idioma == 'pt' else "Inglês"
        separator = ',' if target_language == 'Inglês' else ';'
        formula = formula.replace('[', '').replace(']', '')
        
            # Verifica primeiro se é uma fórmula de contagem que precisa de correção
        if re.search(r'@?(CONT\.IF|COUNTIF|CONT\.SES|COUNTIFS)', formula, re.IGNORECASE):
            formula = self.corrigir_formulas_contagem(formula, target_language)

        # Primeiro: corrigir VLOOKUP/PROCV se necessário
        if (colunas_por_aba and nome_aba_atual and nome_aba_atual in colunas_por_aba):
            formula = self._corrigir_referencia_vlookup(
                formula,
                colunas_planilha=colunas_por_aba[nome_aba_atual],
                language=target_language
            )

        # Depois: traduzir nomes de funções e valores lógicos
        def substituir_funcoes(match):
            nome_funcao = match.group(1)
            return self.translate_function_name(nome_funcao, target_language)

        formula = re.sub(r'\b([A-ZÀ-ÿ]+)\b(?=\()', substituir_funcoes, formula)

        def substituir_logicos(match):
            valor = match.group(0).upper().replace('@', '')
            mapeamento = {
                'pt': {'FALIF': 'FALSO', 'FALIIF': 'FALSO', 'FALS': 'FALSO', 'FALSE': 'FALSO'},
                'en': {'FALIF': 'FALSE', 'FALIIF': 'FALSE', 'FALS': 'FALSE', 'FALSO': 'FALSE'}
            }
            return mapeamento[idioma].get(valor, valor)

        formula = re.sub(
            r'@?(FAL[SI]I?F|FALS[EO]?|FLASE|FALSO|FALSE)',
            substituir_logicos,
            formula,
            flags=re.IGNORECASE
        )

        # Corrigir nomes de abas
        if abas_existentes:
            abas_normalizadas = {aba.upper(): aba for aba in abas_existentes}

            def corrigir_aba(match):
                nome_aba = re.sub(r'^\[\d+\]', '', match.group(1)).strip("'")
                sugestao = difflib.get_close_matches(nome_aba.upper(), abas_normalizadas.keys(), n=1, cutoff=0.4)
                if sugestao:
                    aba_correta = abas_normalizadas[sugestao[0]]
                elif nome_aba.upper() in abas_normalizadas:
                    aba_correta = abas_normalizadas[nome_aba.upper()]
                else:
                    prefix_matches = [key for key in abas_normalizadas if key.startswith(nome_aba.upper())]
                    if prefix_matches:
                        aba_correta = abas_normalizadas[prefix_matches[0]]
                    else:
                        return match.group(0)
                
                return f"'{aba_correta}'!" if ' ' in aba_correta else f"{aba_correta}!"

            padroes_abas = [r"'([^']+)'!", r"\b([A-ZÀ-ÿ0-9_]+)!"]
            for padrao in padroes_abas:
                formula = re.sub(padrao, corrigir_aba, formula)

        # Garantir separadores consistentes
        def substituir_separadores(match):
            args = re.split(r'\s*[,;]\s*', match.group(1))
            return f"({separator.join(args)})"

        formula = re.sub(r'\(([^()]*)\)', substituir_separadores, formula)

        return formula
    
    # def corrigir_formulas_contagem(formula: str, idioma: str) -> str:
    #     """Corrige especificamente fórmulas de contagem entre planilhas"""
    #     if not isinstance(formula, str):
    #         return formula
        
    #     # Padrão para identificar fórmulas de contagem problemáticas
    #     pattern = r'=@?(CONT\.IF|COUNTIF)\(([^,;]+)[,;]([^,;]+)[,;]([^,;]+)[,;]"([^"]+)"\)'
    #     match = re.search(pattern, formula, re.IGNORECASE)
        
    #     if match:
    #         func_name = 'CONT.SES' if idioma == 'pt' else 'COUNTIFS'
    #         range1 = match.group(2).strip()
    #         crit1 = match.group(3).strip()
    #         range2 = match.group(4).strip()
    #         crit2 = f'"{match.group(5)}"'
            
    #         separator = ';' if idioma == 'pt' else ','
    #         return f'={func_name}({range1}{separator}{crit1}{separator}{range2}{separator}{crit2})'
        
    #     return formula
    def corrigir_formulas_contagem(self, formula: str, idioma: str, abas_existentes: list = None) -> str:
        """Corrige fórmulas de contagem entre planilhas com inteligência contextual
        
        Args:
            formula: A fórmula a ser corrigida
            idioma: 'pt' para português ou 'en' para inglês
            abas_existentes: Lista de abas existentes na planilha (opcional)
        
        Returns:
            Fórmula corrigida ou original se não for detectado como fórmula de contagem
        """
        if not isinstance(formula, str) or not formula.startswith('='):
            return formula

        # Padrões avançados para detecção
        patterns = [
            # Padrão básico CONT.SE/COUNTIF
            r'=@?(CONT\.IF|COUNTIF)\(([^,;]+)[,;]([^,;]+)[,;]([^,;]+)[,;]"([^"]+)"\)',
            # Padrão com referências 3D (outras abas)
            r'=@?(CONT\.IF|COUNTIF)\(\'?([^\'!,;]+)\'?!([^,;]+)[,;]([^,;]+)[,;]([^,;]+)[,;]"([^"]+)"\)',
            # Padrão com intervalos inválidos
            r'=@?(CONT\.IF|COUNTIF)\(([^,;]+)[,;]([^,;]+)[,;]([A-Z]+:[A-Z]+)[,;]"([^"]+)"\)'
        ]

        for pattern in patterns:
            match = re.search(pattern, formula, re.IGNORECASE)
            if match:
                func_name = 'CONT.SES' if idioma == 'pt' else 'COUNTIFS'
                groups = match.groups()
                
                # Extrai componentes com base no padrão encontrado
                if len(groups) == 5:  # Padrão básico
                    aba_ref, range1, crit1, range2, crit2 = None, groups[1], groups[2], groups[3], groups[4]
                else:  # Padrão com referência 3D
                    aba_ref, range1, crit1, range2, crit2 = groups[1], groups[2], groups[3], groups[4], groups[5]
                
                # Corrige nome da aba se necessário
                if abas_existentes and aba_ref:
                    aba_correta = self._encontrar_aba_correta(aba_ref, abas_existentes)
                    if aba_correta:
                        range1 = f"'{aba_correta}'!{range1.split('!')[-1]}"
                        range2 = f"'{aba_correta}'!{range2.split('!')[-1]}"
                
                # Corrige intervalos inválidos (como AND:AND)
                if re.match(r'[A-Z]+:[A-Z]+', range2, re.IGNORECASE) and not re.match(r'[A-Z]+\d*:[A-Z]+\d*', range2):
                    range2 = range2.split('!')[-1].split(':')[0] + ':' + range2.split('!')[-1].split(':')[0][0]  # Ex: AND:AND -> A:A
                
                # Verifica se falta referência à aba
                if not any(c in range1 for c in ['!', "'"]):
                    if abas_existentes and len(abas_existentes) > 1:
                        range1 = f"'{abas_existentes[-1]}'!{range1}"
                
                separator = ';' if idioma == 'pt' else ','
                return f'={func_name}({range1}{separator}{crit1}{separator}{range2}{separator}"{crit2}")'
        
        return formula

    def _encontrar_aba_correta(self, aba_ref: str, abas_existentes: list) -> str:
        """Encontra a aba mais provável usando correspondência difusa"""
        aba_ref_clean = aba_ref.strip("'").lower()
        abas_normalizadas = {aba.lower(): aba for aba in abas_existentes}
        
        # 1. Verifica correspondência exata
        if aba_ref_clean in abas_normalizadas:
            return abas_normalizadas[aba_ref_clean]
        
        # 2. Busca por similaridade (difflib)
        matches = difflib.get_close_matches(aba_ref_clean, abas_normalizadas.keys(), n=1, cutoff=0.6)
        if matches:
            return abas_normalizadas[matches[0]]
        
        # 3. Busca por padrões comuns
        padroes = {
            r'dados': ['dados', 'base', 'base_dados'],
            r'processo': ['processos', 'movimento', 'transacoes']
        }
        
        for padrao, alternativas in padroes.items():
            if re.search(padrao, aba_ref_clean):
                for alt in alternativas:
                    if alt in abas_normalizadas:
                        return abas_normalizadas[alt]
        
        return None
    
    
    
    
    
