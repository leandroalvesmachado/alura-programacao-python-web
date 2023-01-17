from validate_docbr import CPF, CNPJ

# class factory
class Documento:
    # ela fica responsável por chamar a classe correta para cada caso
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos esta incorreta!!")


class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj inválido!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

'''
class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)

        if tipo_documento == "cpf":
            if self.cpf_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido!!")
        elif self.tipo_documento == "cnpj":
            if self.cnpj_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido!")
        else:
            raise ValueError("Documento inválido!")


    def __str__(self):
        if self.tipo_documento == "cpf":
            return self.format_cpf()
        elif self.tipo_documento == "cnpj":
            return self.format_cnpj()
    

    def cpf_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida!!")


    def cnpj_valido(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError("Quantidade de dígitos inválida!!")


    def format_cpf(self):
        # fatia_um = self.cpf[:3] # 156
        # fatia_dois = self.cpf[3:6] # 169
        # fatia_tres = self.cpf[6:9] # 879
        # fatia_quatro = self.cpf[9:] # 13
        # return (
        #     "{}.{}.{}-{}".format(
        #         fatia_um,
        #         fatia_dois,
        #         fatia_tres,
        #         fatia_quatro
        #     )
        # )
        
        # utilizando a biblioteca validate_docbr
        mascara = CPF()
        return mascara.mask(self.cpf)

    
    def format_cnpj(self):
        # utilizando a biblioteca validate_docbr
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
'''