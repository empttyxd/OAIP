from typing import Optional



class Projector:
    def __init__(self):
        self._input_source: Optional[str] = None

    def on(self) -> None:
        print("Проектор: включается")

    def off(self) -> None:
        print("Проектор: выключается")

    def set_input(self, source: str) -> None:
        self._input_source = source
        print(f"Проектор: выбран источник → {source.upper()}")

    def set_wide_screen_mode(self) -> None:
        print("Проектор: установлен широкоформатный режим (16:9)")


class Amplifier:
    def on(self) -> None:
        print("Усилитель: включается")

    def off(self) -> None:
        print("Усилитель: выключается")

    def set_dvd(self) -> None:
        print("Усилитель: установлен режим DVD")

    def set_volume(self, level: int) -> None:
        print(f"Усилитель: громкость установлена на {level}%")


class DvdPlayer:
    def __init__(self):
        self._movie: Optional[str] = None

    def on(self) -> None:
        print("DVD-плеер: включается")

    def off(self) -> None:
        print("DVD-плеер: выключается")

    def eject(self) -> None:
        print("DVD-плеер: извлечение диска")

    def play(self, movie: str) -> None:
        self._movie = movie
        print(f"DVD-плеер: воспроизведение фильма '{movie}'")

    def stop(self) -> None:
        print("DVD-плеер: остановка воспроизведения")


class HomeTheaterFacade:

    def __init__(self,
                 amp: Amplifier,
                 projector: Projector,
                 dvd: DvdPlayer):
        self.amp = amp
        self.projector = projector
        self.dvd = dvd

    def watch_movie(self, movie: str) -> None:
        print("\n===== Подготовка к просмотру фильма =====")
        print(f"Фильм: {movie}\n")

        self.amp.on()
        self.amp.set_dvd()
        self.amp.set_volume(15) 
        self.projector.on()
        self.projector.set_input("dvd")
        self.projector.set_wide_screen_mode()

        self.dvd.on()
        self.dvd.play(movie)

        print("\nПриятного просмотра!")

    def end_movie(self) -> None:
        print("\n===== Завершение просмотра =====")

        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()

        self.projector.off()

        self.amp.off()

        print("Система выключена. До свидания\n")



if __name__ == "__main__":
    amp = Amplifier()
    projector = Projector()
    dvd_player = DvdPlayer()

    home_theater = HomeTheaterFacade(amp, projector, dvd_player)
    home_theater.watch_movie("Интерстеллар")


    input("\nНажмите Enter, чтобы закончить просмотр")

    home_theater.end_movie()
