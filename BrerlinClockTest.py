import unittest
from BerlinClock import TimeUnitPart, Hours, Minutes, Seconds, Precondition, Parser, Time, BerlinClock, Lamp, Color


class TestTimeUnits(unittest.TestCase):
    def test_calc(self):
        t = TimeUnitPart(lambda units: (abs((units % 2) - 1)), [Lamp(Color.YELLOW)])

        self.assertEqual(t.calc(0), 1)
        self.assertEqual(t.calc(20), 1)
        self.assertEqual(t.calc(21), 0)
        self.assertEqual(t.display(21), "O")

    def test_display_minutes(self):
        m = Minutes()

        self.assertEquals(m.display(10), "YYOOOOOOOOO OOOO")
        self.assertEquals(m.display(59), "YYRYYRYYRYY YYYY")
        self.assertEquals(m.display(04), "OOOOOOOOOOO YYYY")

    def test_display_hours(self):
        h = Hours()

        self.assertEquals(h.display(24), "RRRR RRRR")
        self.assertEquals(h.display(04), "OOOO RRRR")
        self.assertEquals(h.display(06), "ROOO ROOO")

    def test_display_seconds(self):
        s = Seconds()

        self.assertEquals(s.display(20), "Y")
        self.assertEquals(s.display(21), "O")


class TestParser(unittest.TestCase):
    def test_parse(self):
        time = Parser().parse("01::17:02")
        self.assertTrue(time == Time(1, 17, 02))

    def test_parse_exception(self):
        with self.assertRaises(ValueError):
            Parser().parse("z::17:02")

    def test_berlin_clock(self):
        self.assertEquals(BerlinClock().displayTime("13::17:01"), "O RROO RRRO YYROOOOOOOO YYOO")
        self.assertEquals(BerlinClock().displayTime("23::59:59"), "O RRRR RRRO YYRYYRYYRYY YYYY")
        self.assertEquals(BerlinClock().displayTime("16::16:16"), "Y RRRO ROOO YYROOOOOOOO YOOO")


class TestTime(unittest.TestCase):
    def test_init_time(self):
        t = Time(1, 2, 3)
        self.assertEqual(t.h, 1)
        self.assertEqual(t.m, 2)
        self.assertEqual(t.s, 3)
        self.assertEqual(t.__str__(), "1:2:3")


class TestColor(unittest.TestCase):
    def test_color(self):
        c1 = Color.RED
        c2 = Color.YELLOW

        self.assertEqual(c1.__str__(), "R")
        self.assertEqual(c2.__str__(), "Y")


class TestLamp(unittest.TestCase):
    def test_lamp(self):
        l = Lamp(Color.YELLOW)
        self.assertEqual(l.__str__(), "O")
        l.switchOn()
        self.assertEqual(l.__str__(), "Y")

    def test_precondition(self):
        with self.assertRaises(ValueError):
            Precondition(lambda units: (units >= 1 and units <= 24),
                         "Hour units must be in range: units >= 1 && units <= 24").validate(444)


if __name__ == '__main__':
    unittest.main()