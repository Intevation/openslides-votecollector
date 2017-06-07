from .models import Seat


def setup_default_plan():
    """
    Adds a default seating plan.
    """
    seats = []

    # IG Metall Jugend
    seats.append(Seat(number='01', seating_plan_x_axis=1, seating_plan_y_axis=1))
    seats.append(Seat(number='02', seating_plan_x_axis=2, seating_plan_y_axis=1))
    seats.append(Seat(number='03', seating_plan_x_axis=3, seating_plan_y_axis=1))
    seats.append(Seat(number='04', seating_plan_x_axis=4, seating_plan_y_axis=1))
    seats.append(Seat(number='05', seating_plan_x_axis=5, seating_plan_y_axis=1))
    seats.append(Seat(number='06', seating_plan_x_axis=6, seating_plan_y_axis=1))
    seats.append(Seat(number='07', seating_plan_x_axis=7, seating_plan_y_axis=1))
    seats.append(Seat(number='08', seating_plan_x_axis=8, seating_plan_y_axis=1))
    seats.append(Seat(number='09', seating_plan_x_axis=9, seating_plan_y_axis=1))
    seats.append(Seat(number='10', seating_plan_x_axis=10, seating_plan_y_axis=1))
    seats.append(Seat(number='11', seating_plan_x_axis=11, seating_plan_y_axis=1))
    seats.append(Seat(number='12', seating_plan_x_axis=12, seating_plan_y_axis=1))
    seats.append(Seat(number='13', seating_plan_x_axis=13, seating_plan_y_axis=1))
    seats.append(Seat(number='14', seating_plan_x_axis=14, seating_plan_y_axis=1))
    seats.append(Seat(number='15', seating_plan_x_axis=15, seating_plan_y_axis=1))
    seats.append(Seat(number='16', seating_plan_x_axis=16, seating_plan_y_axis=1))
    seats.append(Seat(number='17', seating_plan_x_axis=17, seating_plan_y_axis=1))
    seats.append(Seat(number='18', seating_plan_x_axis=18, seating_plan_y_axis=1))
    seats.append(Seat(number='19', seating_plan_x_axis=19, seating_plan_y_axis=1))
    seats.append(Seat(number='20', seating_plan_x_axis=20, seating_plan_y_axis=1))
    seats.append(Seat(number='21', seating_plan_x_axis=21, seating_plan_y_axis=1))
    seats.append(Seat(number='22', seating_plan_x_axis=1, seating_plan_y_axis=2))
    seats.append(Seat(number='23', seating_plan_x_axis=2, seating_plan_y_axis=2))
    seats.append(Seat(number='24', seating_plan_x_axis=3, seating_plan_y_axis=2))
    seats.append(Seat(number='25', seating_plan_x_axis=4, seating_plan_y_axis=2))
    seats.append(Seat(number='26', seating_plan_x_axis=5, seating_plan_y_axis=2))
    seats.append(Seat(number='27', seating_plan_x_axis=6, seating_plan_y_axis=2))
    seats.append(Seat(number='28', seating_plan_x_axis=7, seating_plan_y_axis=2))
    seats.append(Seat(number='29', seating_plan_x_axis=8, seating_plan_y_axis=2))
    seats.append(Seat(number='30', seating_plan_x_axis=9, seating_plan_y_axis=2))
    seats.append(Seat(number='31', seating_plan_x_axis=10, seating_plan_y_axis=2))
    seats.append(Seat(number='32', seating_plan_x_axis=11, seating_plan_y_axis=2))
    seats.append(Seat(number='33', seating_plan_x_axis=12, seating_plan_y_axis=2))
    seats.append(Seat(number='34', seating_plan_x_axis=13, seating_plan_y_axis=2))
    seats.append(Seat(number='35', seating_plan_x_axis=14, seating_plan_y_axis=2))
    seats.append(Seat(number='36', seating_plan_x_axis=15, seating_plan_y_axis=2))
    seats.append(Seat(number='37', seating_plan_x_axis=16, seating_plan_y_axis=2))
    seats.append(Seat(number='38', seating_plan_x_axis=17, seating_plan_y_axis=2))
    seats.append(Seat(number='39', seating_plan_x_axis=18, seating_plan_y_axis=2))
    seats.append(Seat(number='40', seating_plan_x_axis=19, seating_plan_y_axis=2))

    # ver.di Jugend
    seats.append(Seat(number='01', seating_plan_x_axis=1, seating_plan_y_axis=3))
    seats.append(Seat(number='02', seating_plan_x_axis=2, seating_plan_y_axis=3))
    seats.append(Seat(number='03', seating_plan_x_axis=3, seating_plan_y_axis=3))
    seats.append(Seat(number='04', seating_plan_x_axis=4, seating_plan_y_axis=3))
    seats.append(Seat(number='05', seating_plan_x_axis=5, seating_plan_y_axis=3))
    seats.append(Seat(number='06', seating_plan_x_axis=6, seating_plan_y_axis=3))
    seats.append(Seat(number='07', seating_plan_x_axis=7, seating_plan_y_axis=3))
    seats.append(Seat(number='08', seating_plan_x_axis=8, seating_plan_y_axis=3))
    seats.append(Seat(number='09', seating_plan_x_axis=9, seating_plan_y_axis=3))
    seats.append(Seat(number='10', seating_plan_x_axis=10, seating_plan_y_axis=3))
    seats.append(Seat(number='11', seating_plan_x_axis=11, seating_plan_y_axis=3))
    seats.append(Seat(number='12', seating_plan_x_axis=12, seating_plan_y_axis=3))
    seats.append(Seat(number='13', seating_plan_x_axis=13, seating_plan_y_axis=3))
    seats.append(Seat(number='14', seating_plan_x_axis=14, seating_plan_y_axis=3))
    seats.append(Seat(number='15', seating_plan_x_axis=15, seating_plan_y_axis=3))
    seats.append(Seat(number='16', seating_plan_x_axis=16, seating_plan_y_axis=3))
    seats.append(Seat(number='17', seating_plan_x_axis=17, seating_plan_y_axis=3))
    seats.append(Seat(number='18', seating_plan_x_axis=18, seating_plan_y_axis=3))
    seats.append(Seat(number='19', seating_plan_x_axis=19, seating_plan_y_axis=3))
    seats.append(Seat(number='20', seating_plan_x_axis=20, seating_plan_y_axis=3))
    seats.append(Seat(number='21', seating_plan_x_axis=21, seating_plan_y_axis=3))

    # IG BCE Jugend
    seats.append(Seat(number='01', seating_plan_x_axis=1, seating_plan_y_axis=4))
    seats.append(Seat(number='02', seating_plan_x_axis=2, seating_plan_y_axis=4))
    seats.append(Seat(number='03', seating_plan_x_axis=3, seating_plan_y_axis=4))
    seats.append(Seat(number='04', seating_plan_x_axis=4, seating_plan_y_axis=4))
    seats.append(Seat(number='05', seating_plan_x_axis=5, seating_plan_y_axis=4))
    seats.append(Seat(number='06', seating_plan_x_axis=6, seating_plan_y_axis=4))
    seats.append(Seat(number='07', seating_plan_x_axis=7, seating_plan_y_axis=4))
    seats.append(Seat(number='08', seating_plan_x_axis=8, seating_plan_y_axis=4))
    seats.append(Seat(number='09', seating_plan_x_axis=9, seating_plan_y_axis=4))
    seats.append(Seat(number='10', seating_plan_x_axis=10, seating_plan_y_axis=4))
    seats.append(Seat(number='11', seating_plan_x_axis=11, seating_plan_y_axis=4))
    seats.append(Seat(number='12', seating_plan_x_axis=12, seating_plan_y_axis=4))
    seats.append(Seat(number='13', seating_plan_x_axis=13, seating_plan_y_axis=4))
    seats.append(Seat(number='14', seating_plan_x_axis=14, seating_plan_y_axis=4))

    # IG BAU Jugend
    seats.append(Seat(number='01', seating_plan_x_axis=1, seating_plan_y_axis=5))
    seats.append(Seat(number='02', seating_plan_x_axis=2, seating_plan_y_axis=5))
    seats.append(Seat(number='03', seating_plan_x_axis=3, seating_plan_y_axis=5))
    seats.append(Seat(number='04', seating_plan_x_axis=4, seating_plan_y_axis=5))
    seats.append(Seat(number='05', seating_plan_x_axis=5, seating_plan_y_axis=5))
    seats.append(Seat(number='06', seating_plan_x_axis=6, seating_plan_y_axis=5))
    seats.append(Seat(number='07', seating_plan_x_axis=7, seating_plan_y_axis=5))

    # Junge Gruppe GdP
    seats.append(Seat(number='01', seating_plan_x_axis=1, seating_plan_y_axis=6))
    seats.append(Seat(number='02', seating_plan_x_axis=2, seating_plan_y_axis=6))
    seats.append(Seat(number='03', seating_plan_x_axis=3, seating_plan_y_axis=6))
    seats.append(Seat(number='04', seating_plan_x_axis=4, seating_plan_y_axis=6))
    seats.append(Seat(number='05', seating_plan_x_axis=5, seating_plan_y_axis=6))
    seats.append(Seat(number='06', seating_plan_x_axis=6, seating_plan_y_axis=6))
    seats.append(Seat(number='07', seating_plan_x_axis=7, seating_plan_y_axis=6))

    # Junge NGG
    seats.append(Seat(number='01', seating_plan_x_axis=1, seating_plan_y_axis=7))
    seats.append(Seat(number='02', seating_plan_x_axis=2, seating_plan_y_axis=7))
    seats.append(Seat(number='03', seating_plan_x_axis=3, seating_plan_y_axis=7))
    seats.append(Seat(number='04', seating_plan_x_axis=4, seating_plan_y_axis=7))
    seats.append(Seat(number='05', seating_plan_x_axis=5, seating_plan_y_axis=7))
    seats.append(Seat(number='06', seating_plan_x_axis=6, seating_plan_y_axis=7))

    # Junge GEW
    seats.append(Seat(number='01', seating_plan_x_axis=1, seating_plan_y_axis=8))
    seats.append(Seat(number='02', seating_plan_x_axis=2, seating_plan_y_axis=8))
    seats.append(Seat(number='03', seating_plan_x_axis=3, seating_plan_y_axis=8))
    seats.append(Seat(number='04', seating_plan_x_axis=4, seating_plan_y_axis=8))
    seats.append(Seat(number='05', seating_plan_x_axis=5, seating_plan_y_axis=8))

    # EVG Jugend
    seats.append(Seat(number='01', seating_plan_x_axis=1, seating_plan_y_axis=9))
    seats.append(Seat(number='02', seating_plan_x_axis=2, seating_plan_y_axis=9))
    seats.append(Seat(number='03', seating_plan_x_axis=3, seating_plan_y_axis=9))
    seats.append(Seat(number='04', seating_plan_x_axis=4, seating_plan_y_axis=9))
    seats.append(Seat(number='05', seating_plan_x_axis=5, seating_plan_y_axis=9))


    # Create seats
    Seat.objects.bulk_create(seats)
