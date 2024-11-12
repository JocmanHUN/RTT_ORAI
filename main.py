import math


class EgyenletMegoldo:
    def masodfoku_egyenlet_megoldas(self, a, b, c):
        if (
            (type(a) not in [int, float])
            or (type(b) not in [int, float])
            or (type(c) not in [int, float])
        ):
            raise TypeError("A, B és C csak számok lehetnek!")
        d = math.pow(b, 2) - 4 * a * c

        if d < 0:
            return None, None
        return (-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)

    def feladatmegoldo(self, a, b, c):
        x1, x2 = self.masodfoku_egyenlet_megoldas(a, b, c)
        if x1 is None:
            print("Nincs valós gyök!")
        else:
            print(f"Az egyenlet gyökei: {x1}, {x2}")
