from abc import ABC, abstractmethod

# receiver
class PaymentProcess:
    def reject(self):
        print("Pago aprovado")
    
    def approve(self):
        print("Pago rechazado")

# abstract command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# concrete command
class RejectPaymentCommand(Command):
    _process: PaymentProcess = None

    def __init__(self, process: PaymentProcess) -> None:
        self._process = process

    def execute(self):
        self._process.reject()

class ApprovePaymentCommand(Command):
    _process: PaymentProcess = None

    def __init__(self, process: PaymentProcess) -> None:
        self._process = process

    def execute(self):
        self._process.approve()

# invoker
class Bank:
    _command: Command = None

    def set_command(self, command: Command):
        self._command = command

    def pay(self):
        self._command.execute()
 

def main():
    payment_process = PaymentProcess()
    approve_command = ApprovePaymentCommand(payment_process)
    reject_command = RejectPaymentCommand(payment_process)
    bank = Bank()

    bank.set_command(approve_command)
    bank.pay()
    bank.set_command(reject_command)
    bank.pay()

main()
