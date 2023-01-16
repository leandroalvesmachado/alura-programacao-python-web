from validate_docbr import CPF, CNPJ

class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        documento = str(documento)
        if self.cpf_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!!")

    def __str__(self):
        return self.format_cpf()
    

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