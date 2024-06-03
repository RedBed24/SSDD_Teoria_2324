import student_pb2
import socket

ID = 5735354
NAME = ["samuel", "espejo"]
EMAIL = f"{NAME[0]}.{NAME[1]}@alu.uclm.es"

IP = "93.189.90.58"
PORT = 2000
SERVER = (IP, PORT)

def print_response(response):
    match response:
        case student_pb2.StudentACK.StudentDataOK.UNKNOWN:
            print("UNKNOWN")
        case student_pb2.StudentACK.StudentDataOK.YES:
            print("YES")
        case student_pb2.StudentACK.StudentDataOK.NO:
            print("NO")

def print_response_better(response):
    print(student_pb2.StudentACK.StudendDataOK.Name(response))

def main():
    student = student_pb2.Student()
    student.id = ID
    student.name.extend(NAME)
    student.email = EMAIL

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(SERVER)
        s.send(student.SerializeToString())

        data = s.recv(1024)

        response = student_pb2.StudentACK().ParseFromString(data)

        print_response(response)


if __name__ == "__main__":
    main()
