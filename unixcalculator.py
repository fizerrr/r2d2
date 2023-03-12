import time
#Funkcja ta przyjmuje jako argument date_str datę w postaci ciągu znaków w formacie YYYY-MM-DD HH:MM:SS i zwraca wartość Unix time w milisekundach.
#  Funkcja korzysta z modułu time w Pythonie, który zapewnia narzędzia do pracy z czasem.
def to_unix_time_ms(date_str):
    """Converts a date string to Unix time in milliseconds."""
    date_time = time.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    unix_time_ms = int(time.mktime(date_time) * 1000)
    return unix_time_ms