from .models import Seat


def setup_default_plan():
    """
    Adds a default seating plan.
    """
    seats = []

    # IG Metall Jugend
    seats.append(Seat(number='IGM 01', seating_plan_x_axis=1, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 02', seating_plan_x_axis=2, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 03', seating_plan_x_axis=3, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 04', seating_plan_x_axis=4, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 05', seating_plan_x_axis=5, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 06', seating_plan_x_axis=6, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 07', seating_plan_x_axis=7, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 08', seating_plan_x_axis=8, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 09', seating_plan_x_axis=9, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 10', seating_plan_x_axis=10, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 11', seating_plan_x_axis=11, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 12', seating_plan_x_axis=12, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 13', seating_plan_x_axis=13, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 14', seating_plan_x_axis=14, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 15', seating_plan_x_axis=15, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 16', seating_plan_x_axis=16, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 17', seating_plan_x_axis=17, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 18', seating_plan_x_axis=18, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 19', seating_plan_x_axis=19, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 20', seating_plan_x_axis=20, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 21', seating_plan_x_axis=21, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 22', seating_plan_x_axis=22, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 23', seating_plan_x_axis=23, seating_plan_y_axis=1))
    seats.append(Seat(number='IGM 24', seating_plan_x_axis=24, seating_plan_y_axis=1))

    # ver.di Jugend
    seats.append(Seat(number='verdi 01', seating_plan_x_axis=1, seating_plan_y_axis=2))
    seats.append(Seat(number='verdi 02', seating_plan_x_axis=2, seating_plan_y_axis=2))
    seats.append(Seat(number='verdi 03', seating_plan_x_axis=3, seating_plan_y_axis=2))
    seats.append(Seat(number='verdi 04', seating_plan_x_axis=4, seating_plan_y_axis=2))
    seats.append(Seat(number='verdi 05', seating_plan_x_axis=5, seating_plan_y_axis=2))
    seats.append(Seat(number='verdi 06', seating_plan_x_axis=6, seating_plan_y_axis=2))
    seats.append(Seat(number='verdi 07', seating_plan_x_axis=7, seating_plan_y_axis=2))
    seats.append(Seat(number='verdi 08', seating_plan_x_axis=8, seating_plan_y_axis=2))
    seats.append(Seat(number='verdi 09', seating_plan_x_axis=9, seating_plan_y_axis=2))
    seats.append(Seat(number='verdi 10', seating_plan_x_axis=10, seating_plan_y_axis=2))
    seats.append(Seat(number='verdi 11', seating_plan_x_axis=11, seating_plan_y_axis=2))
    seats.append(Seat(number='verdi 12', seating_plan_x_axis=12, seating_plan_y_axis=2))
    seats.append(Seat(number='verdi 13', seating_plan_x_axis=13, seating_plan_y_axis=2))
    seats.append(Seat(number='verdi 14', seating_plan_x_axis=14, seating_plan_y_axis=2))
    seats.append(Seat(number='verdi 15', seating_plan_x_axis=15, seating_plan_y_axis=2))
    seats.append(Seat(number='verdi 16', seating_plan_x_axis=16, seating_plan_y_axis=2))

    # IG BCE Jugend
    seats.append(Seat(number='BCE 01', seating_plan_x_axis=1, seating_plan_y_axis=3))
    seats.append(Seat(number='BCE 02', seating_plan_x_axis=2, seating_plan_y_axis=3))
    seats.append(Seat(number='BCE 03', seating_plan_x_axis=3, seating_plan_y_axis=3))
    seats.append(Seat(number='BCE 04', seating_plan_x_axis=4, seating_plan_y_axis=3))
    seats.append(Seat(number='BCE 05', seating_plan_x_axis=5, seating_plan_y_axis=3))
    seats.append(Seat(number='BCE 06', seating_plan_x_axis=6, seating_plan_y_axis=3))
    seats.append(Seat(number='BCE 07', seating_plan_x_axis=7, seating_plan_y_axis=3))
    seats.append(Seat(number='BCE 08', seating_plan_x_axis=8, seating_plan_y_axis=3))
    seats.append(Seat(number='BCE 09', seating_plan_x_axis=9, seating_plan_y_axis=3))
    seats.append(Seat(number='BCE 10', seating_plan_x_axis=10, seating_plan_y_axis=3))
    seats.append(Seat(number='BCE 11', seating_plan_x_axis=11, seating_plan_y_axis=3))

    # Junge IG BAU
    seats.append(Seat(number='BAU 01', seating_plan_x_axis=1, seating_plan_y_axis=4))
    seats.append(Seat(number='BAU 02', seating_plan_x_axis=2, seating_plan_y_axis=4))
    seats.append(Seat(number='BAU 03', seating_plan_x_axis=3, seating_plan_y_axis=4))
    seats.append(Seat(number='BAU 04', seating_plan_x_axis=4, seating_plan_y_axis=4))
    seats.append(Seat(number='BAU 05', seating_plan_x_axis=5, seating_plan_y_axis=4))

    # EVG Jugend
    seats.append(Seat(number='EVG 01', seating_plan_x_axis=1, seating_plan_y_axis=5))
    seats.append(Seat(number='EVG 02', seating_plan_x_axis=2, seating_plan_y_axis=5))
    seats.append(Seat(number='EVG 03', seating_plan_x_axis=3, seating_plan_y_axis=5))
    seats.append(Seat(number='EVG 04', seating_plan_x_axis=4, seating_plan_y_axis=5))

    # junge NGG
    seats.append(Seat(number='NGG 01', seating_plan_x_axis=1, seating_plan_y_axis=6))
    seats.append(Seat(number='NGG 02', seating_plan_x_axis=2, seating_plan_y_axis=6))
    seats.append(Seat(number='NGG 03', seating_plan_x_axis=3, seating_plan_y_axis=6))
    seats.append(Seat(number='NGG 04', seating_plan_x_axis=4, seating_plan_y_axis=6))

    # junge GEW
    seats.append(Seat(number='GEW 01', seating_plan_x_axis=1, seating_plan_y_axis=7))
    seats.append(Seat(number='GEW 02', seating_plan_x_axis=2, seating_plan_y_axis=7))
    seats.append(Seat(number='GEW 03', seating_plan_x_axis=3, seating_plan_y_axis=7))

    # junge Gruppe GdP
    seats.append(Seat(number='GdP 01', seating_plan_x_axis=1, seating_plan_y_axis=8))
    seats.append(Seat(number='GdP 02', seating_plan_x_axis=2, seating_plan_y_axis=8))
    seats.append(Seat(number='GdP 03', seating_plan_x_axis=3, seating_plan_y_axis=8))
    seats.append(Seat(number='GdP 04', seating_plan_x_axis=4, seating_plan_y_axis=8))
    seats.append(Seat(number='GdP 05', seating_plan_x_axis=5, seating_plan_y_axis=8))

    # Create seats
    Seat.objects.bulk_create(seats)
