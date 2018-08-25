
import time
from micropython import const

_RH_RF95_REG_00_FIFO                              = const(0x00)
_RH_RF95_REG_01_OP_MODE                           = const(0x01)
_RH_RF95_REG_02_RESERVED                          = const(0x02)
_RH_RF95_REG_03_RESERVED                          = const(0x03)
_RH_RF95_REG_04_RESERVED                          = const(0x04)
_RH_RF95_REG_05_RESERVED                          = const(0x05)
_RH_RF95_REG_06_FRF_MSB                           = const(0x06)
_RH_RF95_REG_07_FRF_MID                           = const(0x07)
_RH_RF95_REG_08_FRF_LSB                           = const(0x08)
_RH_RF95_REG_09_PA_CONFIG                         = const(0x09)
_RH_RF95_REG_0A_PA_RAMP                           = const(0x0a)
_RH_RF95_REG_0B_OCP                               = const(0x0b)
_RH_RF95_REG_0C_LNA                               = const(0x0c)
_RH_RF95_REG_0D_FIFO_ADDR_PTR                     = const(0x0d)
_RH_RF95_REG_0E_FIFO_TX_BASE_ADDR                 = const(0x0e)
_RH_RF95_REG_0F_FIFO_RX_BASE_ADDR                 = const(0x0f)
_RH_RF95_REG_10_FIFO_RX_CURRENT_ADDR              = const(0x10)
_RH_RF95_REG_11_IRQ_FLAGS_MASK                    = const(0x11)
_RH_RF95_REG_12_IRQ_FLAGS                         = const(0x12)
_RH_RF95_REG_13_RX_NB_BYTES                       = const(0x13)
_RH_RF95_REG_14_RX_HEADER_CNT_VALUE_MSB           = const(0x14)
_RH_RF95_REG_15_RX_HEADER_CNT_VALUE_LSB           = const(0x15)
_RH_RF95_REG_16_RX_PACKET_CNT_VALUE_MSB           = const(0x16)
_RH_RF95_REG_17_RX_PACKET_CNT_VALUE_LSB           = const(0x17)
_RH_RF95_REG_18_MODEM_STAT                        = const(0x18)
_RH_RF95_REG_19_PKT_SNR_VALUE                     = const(0x19)
_RH_RF95_REG_1A_PKT_RSSI_VALUE                    = const(0x1a)
_RH_RF95_REG_1B_RSSI_VALUE                        = const(0x1b)
_RH_RF95_REG_1C_HOP_CHANNEL                       = const(0x1c)
_RH_RF95_REG_1D_MODEM_CONFIG1                     = const(0x1d)
_RH_RF95_REG_1E_MODEM_CONFIG2                     = const(0x1e)
_RH_RF95_REG_1F_SYMB_TIMEOUT_LSB                  = const(0x1f)
_RH_RF95_REG_20_PREAMBLE_MSB                      = const(0x20)
_RH_RF95_REG_21_PREAMBLE_LSB                      = const(0x21)
_RH_RF95_REG_22_PAYLOAD_LENGTH                    = const(0x22)
_RH_RF95_REG_23_MAX_PAYLOAD_LENGTH                = const(0x23)
_RH_RF95_REG_24_HOP_PERIOD                        = const(0x24)
_RH_RF95_REG_25_FIFO_RX_BYTE_ADDR                 = const(0x25)
_RH_RF95_REG_26_MODEM_CONFIG3                     = const(0x26)

_RH_RF95_REG_40_DIO_MAPPING1                      = const(0x40)
_RH_RF95_REG_41_DIO_MAPPING2                      = const(0x41)
_RH_RF95_REG_42_VERSION                           = const(0x42)

_RH_RF95_REG_4B_TCXO                              = const(0x4b)
_RH_RF95_REG_4D_PA_DAC                            = const(0x4d)
_RH_RF95_REG_5B_FORMER_TEMP                       = const(0x5b)
_RH_RF95_REG_61_AGC_REF                           = const(0x61)
_RH_RF95_REG_62_AGC_THRESH1                       = const(0x62)
_RH_RF95_REG_63_AGC_THRESH2                       = const(0x63)
_RH_RF95_REG_64_AGC_THRESH3                       = const(0x64)

# RH_RF95_REG_01_OP_MODE                             0x01
_RH_RF95_LONG_RANGE_MODE                     = const(0x80)
_RH_RF95_ACCESS_SHARED_REG                   = const(0x40)
_RH_RF95_MODE                                = const(0x07)
_RH_RF95_MODE_SLEEP                          = const(0x00)
_RH_RF95_MODE_STDBY                          = const(0x01)
_RH_RF95_MODE_FSTX                           = const(0x02)
_RH_RF95_MODE_TX                             = const(0x03)
_RH_RF95_MODE_FSRX                           = const(0x04)
_RH_RF95_MODE_RXCONTINUOUS                   = const(0x05)
_RH_RF95_MODE_RXSINGLE                       = const(0x06)
_RH_RF95_MODE_CAD                            = const(0x07)

# RH_RF95_REG_09_PA_CONFIG                           0x09
_RH_RF95_PA_SELECT                           = const(0x80)
_RH_RF95_MAX_POWER                           = const(0x70)
_RH_RF95_OUTPUT_POWER                        = const(0x0f)

# RH_RF95_REG_0A_PA_RAMP                             0x0a
_RH_RF95_LOW_PN_TX_PLL_OFF                   = const(0x10)
_RH_RF95_PA_RAMP                             = const(0x0f)
_RH_RF95_PA_RAMP_3_4MS                       = const(0x00)
_RH_RF95_PA_RAMP_2MS                         = const(0x01)
_RH_RF95_PA_RAMP_1MS                         = const(0x02)
_RH_RF95_PA_RAMP_500US                       = const(0x03)
_RH_RF95_PA_RAMP_250US                       = const(0x04)
_RH_RF95_PA_RAMP_125US                       = const(0x05)
_RH_RF95_PA_RAMP_100US                       = const(0x06)
_RH_RF95_PA_RAMP_62US                        = const(0x07)
_RH_RF95_PA_RAMP_50US                        = const(0x08)
_RH_RF95_PA_RAMP_40US                        = const(0x09)
_RH_RF95_PA_RAMP_31US                        = const(0x0a)
_RH_RF95_PA_RAMP_25US                        = const(0x0b)
_RH_RF95_PA_RAMP_20US                        = const(0x0c)
_RH_RF95_PA_RAMP_15US                        = const(0x0d)
_RH_RF95_PA_RAMP_12US                        = const(0x0e)
_RH_RF95_PA_RAMP_10US                        = const(0x0f)

# RH_RF95_REG_0B_OCP                                 0x0b
_RH_RF95_OCP_ON                              = const(0x20)
_RH_RF95_OCP_TRIM                            = const(0x1f)

# RH_RF95_REG_0C_LNA                                 0x0c
_RH_RF95_LNA_GAIN                            = const(0xe0)
_RH_RF95_LNA_BOOST                           = const(0x03)
_RH_RF95_LNA_BOOST_DEFAULT                   = const(0x00)
_RH_RF95_LNA_BOOST_150PC                     = const(0x11)

# RH_RF95_REG_11_IRQ_FLAGS_MASK                      0x11
_RH_RF95_RX_TIMEOUT_MASK                     = const(0x80)
_RH_RF95_RX_DONE_MASK                        = const(0x40)
_RH_RF95_PAYLOAD_CRC_ERROR_MASK              = const(0x20)
_RH_RF95_VALID_HEADER_MASK                   = const(0x10)
_RH_RF95_TX_DONE_MASK                        = const(0x08)
_RH_RF95_CAD_DONE_MASK                       = const(0x04)
_RH_RF95_FHSS_CHANGE_CHANNEL_MASK            = const(0x02)
_RH_RF95_CAD_DETECTED_MASK                   = const(0x01)

# RH_RF95_REG_12_IRQ_FLAGS                           0x12
_RH_RF95_RX_TIMEOUT                          = const(0x80)
_RH_RF95_RX_DONE                             = const(0x40)
_RH_RF95_PAYLOAD_CRC_ERROR                   = const(0x20)
_RH_RF95_VALID_HEADER                        = const(0x10)
_RH_RF95_TX_DONE                             = const(0x08)
_RH_RF95_CAD_DONE                            = const(0x04)
_RH_RF95_FHSS_CHANGE_CHANNEL                 = const(0x02)
_RH_RF95_CAD_DETECTED                        = const(0x01)

# RH_RF95_REG_18_MODEM_STAT                          0x18
_RH_RF95_RX_CODING_RATE                      = const(0xe0)
_RH_RF95_MODEM_STATUS_CLEAR                  = const(0x10)
_RH_RF95_MODEM_STATUS_HEADER_INFO_VALID      = const(0x08)
_RH_RF95_MODEM_STATUS_RX_ONGOING             = const(0x04)
_RH_RF95_MODEM_STATUS_SIGNAL_SYNCHRONIZED    = const(0x02)
_RH_RF95_MODEM_STATUS_SIGNAL_DETECTED        = const(0x01)

# RH_RF95_REG_1C_HOP_CHANNEL                         0x1c
_RH_RF95_PLL_TIMEOUT                         = const(0x80)
_RH_RF95_RX_PAYLOAD_CRC_IS_ON                = const(0x40)
_RH_RF95_FHSS_PRESENT_CHANNEL                = const(0x3f)

# RH_RF95_REG_1D_MODEM_CONFIG1                       0x1d
_RH_RF95_BW                                  = const(0xc0)
_RH_RF95_BW_125KHZ                           = const(0x00)
_RH_RF95_BW_250KHZ                           = const(0x40)
_RH_RF95_BW_500KHZ                           = const(0x80)
_RH_RF95_BW_RESERVED                         = const(0xc0)
_RH_RF95_CODING_RATE                         = const(0x38)
_RH_RF95_CODING_RATE_4_5                     = const(0x00)
_RH_RF95_CODING_RATE_4_6                     = const(0x08)
_RH_RF95_CODING_RATE_4_7                     = const(0x10)
_RH_RF95_CODING_RATE_4_8                     = const(0x18)
_RH_RF95_IMPLICIT_HEADER_MODE_ON             = const(0x04)
_RH_RF95_RX_PAYLOAD_CRC_ON                   = const(0x02)
_RH_RF95_LOW_DATA_RATE_OPTIMIZE              = const(0x01)

# RH_RF95_REG_1E_MODEM_CONFIG2                       0x1e
_RH_RF95_SPREADING_FACTOR                    = const(0xf0)
_RH_RF95_SPREADING_FACTOR_64CPS              = const(0x60)
_RH_RF95_SPREADING_FACTOR_128CPS             = const(0x70)
_RH_RF95_SPREADING_FACTOR_256CPS             = const(0x80)
_RH_RF95_SPREADING_FACTOR_512CPS             = const(0x90)
_RH_RF95_SPREADING_FACTOR_1024CPS            = const(0xa0)
_RH_RF95_SPREADING_FACTOR_2048CPS            = const(0xb0)
_RH_RF95_SPREADING_FACTOR_4096CPS            = const(0xc0)
_RH_RF95_TX_CONTINUOUS_MOE                   = const(0x08)
_RH_RF95_AGC_AUTO_ON                         = const(0x04)
_RH_RF95_SYM_TIMEOUT_MSB                     = const(0x03)

# RH_RF95_REG_4D_PA_DAC                              0x4d
_RH_RF95_PA_DAC_DISABLE                      = const(0x04)
_RH_RF95_PA_DAC_ENABLE                       = const(0x07)

# The crystal oscillator frequency of the module
_RH_RF95_FXOSC = 32000000.0

# The Frequency Synthesizer step = RH_RF95_FXOSC / 2^^19
_RH_RF95_FSTEP = (_RH_RF95_FXOSC / 524288)

# RadioHead specific compatibility constants.
_RH_BROADCAST_ADDRESS = const(0xFF)

# User facing constants:
SLEEP_MODE   = 0b000
STANDBY_MODE = 0b001
FS_TX_MODE   = 0b010
TX_MODE      = 0b011
FS_RX_MODE   = 0b100
RX_MODE      = 0b101
# pylint: enable=bad-whitespace


# Disable the too many instance members warning.  Pylint has no knowledge
# of the context and is merely guessing at the proper amount of members.  This
# is a complex chip which requires exposing many attributes and state.  Disable
# the warning to work around the error.
# pylint: disable=too-many-instance-attributes

class RFM9x:
    # Global buffer to hold data sent and received with the chip.  This must be
    # at least as large as the FIFO on the chip (256 bytes)!  Keep this on the
    # class level to ensure only one copy ever exists (with the trade-off that
    # this is NOT re-entrant or thread safe code by design).
    _BUFFER = bytearray(10)

    class _RegisterBits:
        # Class to simplify access to the many configuration bits avaialable
        # on the chip's registers.  This is a subclass here instead of using
        # a higher level module to increase the efficiency of memory usage
        # (all of the instances of this bit class will share the same buffer
        # used by the parent RFM69 class instance vs. each having their own
        # buffer and taking too much memory).

        # Quirk of pylint that it requires public methods for a class.  This
        # is a decorator class in Python and by design it has no public methods.
        # Instead it uses dunder accessors like get and set below.  For some
        # reason pylint can't figure this out so disable the check.
        # pylint: disable=too-few-public-methods

        # Again pylint fails to see the true intent of this code and warns
        # against private access by calling the write and read functions below.
        # This is by design as this is an internally used class.  Disable the
        # check from pylint.
        # pylint: disable=protected-access

        def __init__(self, address, *, offset=0, bits=1):
            assert 0 <= offset <= 7
            assert 1 <= bits <= 8
            assert (offset + bits) <= 8
            self._address = address
            self._mask = 0
            for _ in range(bits):
                self._mask <<= 1
                self._mask |= 1
            self._mask <<= offset
            self._offset = offset

        def __get__(self, obj, objtype):
            reg_value = obj._read_u8(self._address)
            return (reg_value & self._mask) >> self._offset

        def __set__(self, obj, val):
            reg_value = obj._read_u8(self._address)
            reg_value &= ~self._mask
            reg_value |= (val & 0xFF) << self._offset
            obj._write_u8(self._address, reg_value)

    operation_mode = _RegisterBits(_RH_RF95_REG_01_OP_MODE, bits=3)

    low_frequency_mode = _RegisterBits(_RH_RF95_REG_01_OP_MODE, offset=3, bits=1)

    modulation_type = _RegisterBits(_RH_RF95_REG_01_OP_MODE, offset=5, bits=2)

    # Long range/LoRa mode can only be set in sleep mode!
    long_range_mode = _RegisterBits(_RH_RF95_REG_01_OP_MODE, offset=7, bits=1)

    output_power = _RegisterBits(_RH_RF95_REG_09_PA_CONFIG, bits=4)

    max_power = _RegisterBits(_RH_RF95_REG_09_PA_CONFIG, offset=4, bits=3)

    pa_select = _RegisterBits(_RH_RF95_REG_09_PA_CONFIG, offset=7, bits=1)

    pa_dac = _RegisterBits(_RH_RF95_REG_4D_PA_DAC, bits=3)

    dio0_mapping = _RegisterBits(_RH_RF95_REG_40_DIO_MAPPING1, offset=6, bits=2)

    tx_done = _RegisterBits(_RH_RF95_REG_12_IRQ_FLAGS, offset=3, bits=1)

    rx_done = _RegisterBits(_RH_RF95_REG_12_IRQ_FLAGS, offset=6, bits=1)

    def __init__(self, spi, cs, reset, frequency, *, preamble_length=8,
                 high_power=True, baudrate=5000000):
        self.high_power = high_power
        self.cs=cs
        
    def _read_into(self, address, buf, length=None):
        self.cs.value(1) # reset to default
        self.cs.value(0) # pull low for spi access
        # Read a number of bytes from the specified address into the provided
        # buffer.  If length is not specified (the default) the entire buffer
        # will be filled.
        if length is None:
            length = len(buf)
        self._BUFFER[0] = address & 0x7F
        print("before:\n",self._BUFFER)
        writebuf=bytearray([self._BUFFER[0]])
        spi.write(writebuf)
        print("middle:\n",self._BUFFER)
        #newbuf=bytearray([buf[0]])
        #device.write(newbuf)
        #device.readinto(buf[0:length])
        newbuf=buf[0:length]
        spi.readinto(newbuf)
        buf[0:len(newbuf)]=newbuf
        print("after:\n",self._BUFFER)
        self.cs.value(1) # reset to default
        
    def _read_u8(self, address):
        # Read a single byte from the provided address and return it.
        self._read_into(address, self._BUFFER, length=1)
        return self._BUFFER[0]

from machine import Pin
from machine import SPI


sck=Pin(5)
mosi=Pin(18)
miso=Pin(19)
cs = Pin(12, Pin.OUT)
reset=Pin(13)



address=const(0x02) #-- seems constant across widgets

spi=SPI(2,baudrate=5000000,sck=sck,mosi=mosi,miso=miso)

rfm9x = RFM9x(spi, cs, reset, 915.0)

mybuff=bytearray(10)

#cs.value(0)
#rfm9x._read_into(address,mybuff,length=1)
#print(mybuff[0])

print(rfm9x._read_u8(address))
#cs.value(1)



spi.deinit()

