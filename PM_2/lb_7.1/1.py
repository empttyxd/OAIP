from abc import ABC, abstractmethod


class TextPrinter(ABC):
    @abstractmethod
    def print_text(self) -> None:
        pass


class SimpleTextPrinter(TextPrinter):
    def __init__(self, text: str):
        self.text = text

    def print_text(self) -> None:
        print(self.text)


class TextDecorator(TextPrinter):
    def __init__(self, printer: TextPrinter):
        self._printer = printer

    def print_text(self) -> None:
        self._printer.print_text()


class UpperCaseDecorator(TextDecorator):
    def print_text(self) -> None:
        original = self._printer.print_text.__self__.text if hasattr(self._printer, 'text') else ""
        print(original.upper())


class BorderDecorator(TextDecorator):
    def print_text(self) -> None:
        text = self._printer.print_text.__self__.text if hasattr(self._printer, 'text') else ""
        width = len(text) + 4
        print("+" + "-" * width + "+")
        print(f"| {text} |")
        print("+" + "-" * width + "+")


class ExclamationDecorator(TextDecorator):
    def __init__(self, printer: TextPrinter, count: int = 3):
        super().__init__(printer)
        self.count = count

    def print_text(self) -> None:
        text = self._printer.print_text.__self__.text if hasattr(self._printer, 'text') else ""
        print(text + "!" * self.count)


if __name__ == "__main__":
    print("=== Тесты декораторов ===\n")

    simple = SimpleTextPrinter("Привет, мир")
    print("Обычный текст:")
    simple.print_text()
    print()

    upper = UpperCaseDecorator(simple)
    print("Только верхний регистр:")
    upper.print_text()
    print()

    border = BorderDecorator(simple)
    print("Только рамка:")
    border.print_text()
    print()

    excl = ExclamationDecorator(simple, count=5)
    print("Только восклицательные знаки:")
    excl.print_text()
    print()

    upper_border = BorderDecorator(UpperCaseDecorator(simple))
    print("Верхний регистр + рамка:")
    upper_border.print_text()
    print()

    full = BorderDecorator(
        UpperCaseDecorator(
            ExclamationDecorator(simple, count=4)
        )
    )
    print("Всё вместе (восклицания → uppercase → рамка):")
    full.print_text()
    print()

    excl_border = BorderDecorator(ExclamationDecorator(simple))
    print("Восклицания + рамка:")
    excl_border.print_text()
