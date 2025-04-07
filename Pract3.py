class Lexer:
    def __init__(self):
        self.keywords = {
            'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
            'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
            'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
            'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while'
        }
        
        self.operators = {
            '+', '-', '*', '/', '%', '=', '<', '>', '!', '&', '|', '^', '~',
            '+=', '-=', '*=', '/=', '%=', '==', '<=', '>=', '!=', '&&', '||',
            '>>=', '<<=', '++', '--'
        }
        
        self.punctuations = {'(', ')', '{', '}', '[', ']', ',', ';', '.'} 
        self.symbols = set()
        self.errors = []
        self.tokens = []
        self.current_index = 0
        self.line_number = 1

    def is_whitespace(self, ch):
        return ch in ' \t\n\r'
    
    def is_letter(self, ch):
        return 'a' <= ch.lower() <= 'z'
    
    def is_digit(self, ch):
        return '0' <= ch <= '9'
    
    def get_next_non_whitespace(self, code):
        idx = self.current_index + 1
        while idx < len(code) and self.is_whitespace(code[idx]):
            idx += 1
        return code[idx] if idx < len(code) else None

    def extract_lexeme(self, code):
        lexeme = ''
        start_idx = self.current_index

        while self.current_index < len(code) and not self.is_whitespace(code[self.current_index]) and \
              code[self.current_index] not in self.operators and \
              code[self.current_index] not in self.punctuations:
            lexeme += code[self.current_index]
            self.current_index += 1
        
        self.current_index -= 1 
        
        if lexeme in self.keywords:
            return ('Keyword', lexeme)
        
        if lexeme:
            if self.is_letter(lexeme[0]) or lexeme[0] == '_':
                if all(self.is_letter(c) or self.is_digit(c) or c == '_' for c in lexeme[1:]):
                    next_char = self.get_next_non_whitespace(code)
                    if next_char != '(': 
                        self.symbols.add(lexeme)
                    return ('Identifier', lexeme)
            
            if self.is_digit(lexeme[0]):
                try:
                    float(lexeme)
                    return ('Constant', lexeme)
                except ValueError:
                    pass
            
            self.errors.append(lexeme)
            return None

        return None

    def extract_string(self, code):
        string_value = '"'
        self.current_index += 1 
        
        while self.current_index < len(code):
            char = code[self.current_index]
            string_value += char
            
            if char == '"':
                break
            self.current_index += 1
        
        return ('String', string_value)

    def extract_operator(self, code):
        op = code[self.current_index]
        next_idx = self.current_index + 1
        
        if next_idx < len(code):
            combined_op = op + code[next_idx]
            if combined_op in self.operators:
                self.current_index += 1
                return ('Operator', combined_op)
        
        return ('Operator', op)

    def ignore_comment(self, code):
        if code[self.current_index:self.current_index + 2] == '//':
            while self.current_index < len(code) and code[self.current_index] != '\n':
                self.current_index += 1
        elif code[self.current_index:self.current_index + 2] == '/*':
            self.current_index += 2
            while self.current_index < len(code) - 1:
                if code[self.current_index:self.current_index + 2] == '*/':
                    self.current_index += 1
                    break
                if code[self.current_index] == '\n':
                    self.line_number += 1
                self.current_index += 1

    def analyze_code(self, code):
        self.tokens = []
        self.current_index = 0
        
        while self.current_index < len(code):
            ch = code[self.current_index]
            
            if self.is_whitespace(ch):
                if ch == '\n':
                    self.line_number += 1
                self.current_index += 1
                continue
            
            if ch == '/' and self.current_index + 1 < len(code) and code[self.current_index + 1] in '/*':
                self.ignore_comment(code)
                self.current_index += 1
                continue
            
            if self.is_letter(ch) or ch == '_' or self.is_digit(ch):
                token = self.extract_lexeme(code)
                if token:
                    self.tokens.append(token)
            
            elif ch == '"':
                token = self.extract_string(code)
                self.tokens.append(token)
            
            elif ch in self.operators:
                token = self.extract_operator(code)
                self.tokens.append(token)
            
            elif ch in self.punctuations:
                self.tokens.append(('Punctuation', ch))
            
            self.current_index += 1
        
        return self.tokens

    def analyze_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            tokens = self.analyze_code(content)
            
            print("TOKENS")
            for token_type, value in tokens:
                print(f"{token_type}: {value}")
            
            if self.errors:
                print("\nLEXICAL ERRORS")
                for error in self.errors:
                    print(f"{error} is not a valid lexeme")
            
            print("\nSYMBOL TABLE")
            for idx, identifier in enumerate(sorted(self.symbols), 1):
                print(f"{idx}) {identifier}")
            
        except FileNotFoundError:
            print(f"Error: Cannot open file '{file_path}'")

if __name__ == "__main__":
    file_path = "d:\\VI-SEM\\DLP\\Practical\\test4.c"
    lexer = Lexer()
    lexer.analyze_file(file_path)
