from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform, VivadoProgrammer

# IOs ----------------------------------------------------------------------------------------------

_io = [
    ("led",  0, Pins("H17"), IOStandard("LVCMOS33")),
    ("led",  1, Pins("K15"), IOStandard("LVCMOS33")),
    ("led",  2, Pins("J13"), IOStandard("LVCMOS33")),
    ("led",  3, Pins("N14"), IOStandard("LVCMOS33")),
    ("led",  4, Pins("R18"), IOStandard("LVCMOS33")),
    ("led",  5, Pins("V17"), IOStandard("LVCMOS33")),
    ("led",  6, Pins("U17"), IOStandard("LVCMOS33")),
    ("led",  7, Pins("U16"), IOStandard("LVCMOS33")),
    ("led",  8, Pins("V16"), IOStandard("LVCMOS33")),
    ("led",  9, Pins("T15"), IOStandard("LVCMOS33")),
    ("led", 10, Pins("U14"), IOStandard("LVCMOS33")),
    ("led", 11, Pins("T16"), IOStandard("LVCMOS33")),
    ("led", 12, Pins("V15"), IOStandard("LVCMOS33")),
    ("led", 13, Pins("V14"), IOStandard("LVCMOS33")),
    ("led", 14, Pins("V12"), IOStandard("LVCMOS33")),
    ("led", 15, Pins("V11"), IOStandard("LVCMOS33")),

    ("sw",  0, Pins("J15"), IOStandard("LVCMOS33")),
    ("sw",  1, Pins("L16"), IOStandard("LVCMOS33")),
    ("sw",  2, Pins("M13"), IOStandard("LVCMOS33")),
    ("sw",  3, Pins("R15"), IOStandard("LVCMOS33")),
    ("sw",  4, Pins("R17"), IOStandard("LVCMOS33")),
    ("sw",  5, Pins("T18"), IOStandard("LVCMOS33")),
    ("sw",  6, Pins("U18"), IOStandard("LVCMOS33")),
    ("sw",  7, Pins("R13"), IOStandard("LVCMOS33")),
    ("sw",  8, Pins("T8"), IOStandard("LVCMOS33")),
    ("sw",  9, Pins("U8"), IOStandard("LVCMOS33")),
    ("sw", 10, Pins("R16"), IOStandard("LVCMOS33")),
    ("sw", 11, Pins("T13"), IOStandard("LVCMOS33")),
    ("sw", 12, Pins("H6"), IOStandard("LVCMOS33")),
    ("sw", 13, Pins("U12"), IOStandard("LVCMOS33")),
    ("sw", 14, Pins("U11"), IOStandard("LVCMOS33")),
    ("sw", 15, Pins("V10"), IOStandard("LVCMOS33")),
    
    ("pwm__", 1, Pins("E6"), IOStandard("LVCMOS33")),
  
    ("btnc", 0, Pins("N17"), IOStandard("LVCMOS33")),
    ("btnd", 0, Pins("P18"), IOStandard("LVCMOS33")),
    ("btnu", 0, Pins("M18"), IOStandard("LVCMOS33")),
    ("btnr", 0, Pins("M17"), IOStandard("LVCMOS33")),
    ("btnl", 0, Pins("P17"), IOStandard("LVCMOS33")),

    ("ledRGB", 1,
        Subsignal("r", Pins("N15")),
        Subsignal("g", Pins("M16")),
        Subsignal("b", Pins("R12")),
        IOStandard("LVCMOS33")),

    ("ledRGB", 2,
        Subsignal("r", Pins("N16")),
        Subsignal("g", Pins("R11")),
        Subsignal("b", Pins("G14")),
        IOStandard("LVCMOS33")),
       
    ("display_cs_n",  0, Pins("J17 J18 J14 P14 K2 U13 T9 T14"), IOStandard("LVCMOS33")),
    ("display_abcdefg",  0, Pins("T10 R10 K16 K13 P15 T11 L18 H15"), IOStandard("LVCMOS33")),
  	
    ("vga_red", 0, Pins("A3"), IOStandard("LVCMOS33")),
    ("vga_red", 1, Pins("B4"), IOStandard("LVCMOS33")),
    ("vga_red", 2, Pins("C5"), IOStandard("LVCMOS33")),
    ("vga_red", 3, Pins("A4"), IOStandard("LVCMOS33")),
    ("vga_green", 0, Pins("C6"), IOStandard("LVCMOS33")),
    ("vga_green", 1, Pins("A5"), IOStandard("LVCMOS33")),
    ("vga_green", 2, Pins("B6"), IOStandard("LVCMOS33")),
    ("vga_green", 3, Pins("A6"), IOStandard("LVCMOS33")),
    ("vga_blue", 0, Pins("B7"), IOStandard("LVCMOS33")),
    ("vga_blue", 1, Pins("C7"), IOStandard("LVCMOS33")),
    ("vga_blue", 2, Pins("D7"), IOStandard("LVCMOS33")),
    ("vga_blue", 3, Pins("D8"), IOStandard("LVCMOS33")),
    ("hsync", 0, Pins("B11"), IOStandard("LVCMOS33")),
    ("vsync", 0, Pins("B12"), IOStandard("LVCMOS33")),
    
    ("cpu_reset", 0, Pins("C12"), IOStandard("LVCMOS33")),
    
    ("clk", 0, Pins("E3"), IOStandard("LVCMOS33")),

    ("serial", 0,
        Subsignal("tx", Pins("D4")),
        Subsignal("rx", Pins("C4")),
        IOStandard("LVCMOS33"),
    ),

    ("ddram", 0,
        Subsignal("a", Pins(
            "M4 P4 M6 T1 L3 P5 M2 N1",
            "L4 N5 R2 K5 N6"),
            IOStandard("SSTL18_II")),
        Subsignal("ba", Pins("P2 P3 R1"), IOStandard("SSTL18_II")),
        Subsignal("ras_n", Pins("N4"), IOStandard("SSTL18_II")),
        Subsignal("cas_n", Pins("L1"), IOStandard("SSTL18_II")),
        Subsignal("we_n", Pins("N2"), IOStandard("SSTL18_II")),
        Subsignal("dm", Pins("T6 U1"), IOStandard("SSTL18_II")),
        Subsignal("dq", Pins(
            "R7 V6 R8 U7 V7 R6 U6 R5",
            "T5 U3 V5 U4 V4 T4 V1 T3"),
            IOStandard("SSTL18_II"),
            Misc("IN_TERM=UNTUNED_SPLIT_50")),
        Subsignal("dqs_p", Pins("U9 U2"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("dqs_n", Pins("V9 V2"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("clk_p", Pins("L6"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("clk_n", Pins("L5"), IOStandard("DIFF_SSTL18_II")),
        Subsignal("cke", Pins("M1"), IOStandard("SSTL18_II")),
        Subsignal("odt", Pins("M3"), IOStandard("SSTL18_II")),
        Subsignal("cs_n", Pins("K6"), IOStandard("SSTL18_II")),
        Misc("SLEW=FAST"),
    ),

    ("eth_clocks", 0,
        Subsignal("ref_clk", Pins("D5")),
        IOStandard("LVCMOS33"),
    ),

    ("eth", 0,
        Subsignal("rst_n", Pins("B3")),
        Subsignal("rx_data", Pins("C11 D10")),
        Subsignal("crs_dv", Pins("D9")),
        Subsignal("tx_en", Pins("B9")),
        Subsignal("tx_data", Pins("A10 A8")),
        Subsignal("mdc", Pins("C9")),
        Subsignal("mdio", Pins("A9")),
        Subsignal("rx_er", Pins("C10")),
        Subsignal("int_n", Pins("D8")),
        IOStandard("LVCMOS33")
     ),
]

# Platform -----------------------------------------------------------------------------------------

class Platform(XilinxPlatform):
    default_clk_name = "clk"
    default_clk_period = 1e9/100e6

    def __init__(self):
        XilinxPlatform.__init__(self, "xc7a100t-CSG324-1", _io, toolchain="vivado")
        self.add_platform_command("set_property INTERNAL_VREF 0.750 [get_iobanks 34]")

    def create_programmer(self):
        return VivadoProgrammer()

    def do_finalize(self, fragment):
        XilinxPlatform.do_finalize(self, fragment)
