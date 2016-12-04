
import urllib.request
from xml.dom.minidom import parseString

def GetEuroToUSDRate():
    CurrencyRates = 'http://www.ecb.int/stats/eurofxref/eurofxref-daily.xml'
    File = urllib.request.urlopen(CurrencyRates)
    Data = File.read()
    lineStr = str( Data, encoding='utf8' )
    File.close()
    i = lineStr.find("""<Cube currency=\'USD\'""")
    j = lineStr.find("'/",i)
    return float(lineStr[i+27:j])

def GetXMLDocFromUrl(Url):
    File = urllib.request.urlopen(Url)
    Data = File.read()
    File.close()
    dom = parseString(Data)
    return dom

def GetSingleElement(dom,tag):
    xmlTag = dom.getElementsByTagName(tag)[0].toxml()
    StartTag = '<'+tag+'>'
    EndTag = '</'+tag+'>'
    return xmlTag.replace(StartTag,'').replace(EndTag,'')

def GetWeatherInfo():
    KATTAddress = 'http://www.weather.gov/data/current_obs/KATT.xml'
    dom = GetXMLDocFromUrl(KATTAddress)
    F = GetSingleElement(dom,'temp_f')
    P = GetSingleElement(dom,'pressure_in')
    D = GetSingleElement(dom,'dewpoint_f')
    return float(F),float(P),float(D)

def RelativeHumidity(Fahrenheit, DewPoint):
        Tc = 5.0 / 9.0 * (Fahrenheit - 32.0)
        Tdc = 5.0 / 9.0 * (DewPoint - 32.0)
        Es = 6.11 * (10.0 ** (7.5 * Tc / (237.7 + Tc)))
        E = 6.11 * (10.0 ** (7.5 * Tdc / (237.7 + Tdc)))
        return int(round((E / Es) * 100))
    
def HeatIndex(RelHumidity,FTemp):
    T = FTemp
    RH = RelHumidity
    HI = 16.923 + (0.185212 * T) + (5.37941 * RH) - (0.100254 * T * RH)\
    + (0.00941695 * T ** 2) + (0.00728898 * RH ** 2) + (0.000345372 * T ** 2 * RH)\
    - (0.000814971 * T * RH ** 2) + (0.0000102102 * T ** 2 * RH ** 2) - (0.000038646 * T ** 3)\
    + (0.0000291583 * RH ** 3) + (0.00000142721 * T ** 3 * RH) + (0.000000197483 * T * RH ** 3)\
    - (0.0000000218429 * T ** 3 * RH ** 2) + (0.000000000843296 * T ** 2 * RH ** 3)\
    - (0.0000000000481975 * T ** 3 * RH ** 3)
    return round(HI,2)

def Fahr2Celsius(Fahrenheit):
    return 5.0 / 9.0 * (Fahrenheit - 32.0)

def Hypotenuse(Side1, Side2):
    return (Side1**2 + Side2**2)**.5

def PlaySound(Frequency,Seconds):
    import winsound
    winsound.Beep(int(Frequency),int(Seconds)*1000)

def EjectCD():
    import ctypes
    ctypes.windll.WINMM.mciSendStringW(u"open D: type cdaudio alias d_drive", None, 0, None)
    ctypes.windll.WINMM.mciSendStringW(u"set d_drive door open", None, 0, None)
    return


