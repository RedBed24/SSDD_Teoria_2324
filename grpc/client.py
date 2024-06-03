import grpc

import exercise_pb2
import exercise_pb2_grpc

HOST = "93.189.90.58"
PORT = 2000
SERVER = f"{HOST}:{PORT}"

def main():
    mensaje = exercise_pb2.ID()
    mensaje.dni = ""
    mensaje.email = ""
    mensaje.fullname = ""

    with grpc.insecure_channel(SERVER) as ch:
        stub = exercise_pb2_grpc.IdentifyStub(ch)
        respuesta = stub.sendID(mensaje)

    print(respuesta.reason)

    if respuesta.success:
        print("Yay! :D")

if __name__ == '__main__':
    main()

