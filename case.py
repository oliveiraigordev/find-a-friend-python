class AlgumaCoisa:
    def __enter__(self):
        print("estou entrando")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("estou saindo")

with AlgumaCoisa() as something:
    # raise Exception("erro")
    print("estou no meio")

# exc_type: tipo de exceção
# exc_val: valor da exceção
# exc_tb: tracebrack
