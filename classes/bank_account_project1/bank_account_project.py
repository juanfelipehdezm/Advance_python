from datetime import timedelta, datetime,timezone

#time_zone class 
class TimeZone:
    """Represents a time zone with a name and offset in hours and minutes.

        Args:
            name (str): The name of the time zone.
            offset_hours (int): The hour offset of the time zone.
            offset_minutes (int): The minute offset of the time zone.

        Returns:
            None

        Raises:
            ValueError: If the timezone name is empty, hour offset is not an integer, minute offset is not an integer,
                        minute offset is not between -59 and 59, or offset is not between -12:00 and 14:00.

        Examples:
            tz = TimeZone('GMT', 0, 0)
        """

    """Returns the offset of the time zone."""
    """Returns the name of the time zone."""
    """Compares the current time zone with another time zone for equality."""
    """Returns a string representation of the time zone."""

    def __init__(self, name: str, offset_hours: int, offset_minutes: int):
        if name is None:
            raise ValueError("Timezone name can not be empty")
        self._name = name.strip()

        if not isinstance(offset_hours, int):
            raise ValueError("Hour offset must be an integer")
        

        if not isinstance(offset_minutes, int):
            raise ValueError("Hour offset must be an integer")

        if offset_minutes > 59 or offset_minutes < -59:
            raise ValueError("Minutes offset must be between -59 and 59")

        offset = timedelta(hours=offset_hours, minutes=offset_minutes)

        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes= 0):
            raise ValueError("Offset must be between -12:00 and 14:00")

        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes
        self._offset = offset


    @property
    def offset(self):
        return self._offset
    
    @property
    def name(self):
        return self._name
    
    def __eq__(self, other_timezone):
        return (isinstance(other_timezone, TimeZone) and
                self._name == other_timezone._name and
                self._offset == other_timezone._offset)

    def __repr__(self):
        return (f"TimeZone(name='{self.name}'", 
                f"offset_hours= {self._offset_hours}", 
                f"offset_minutes = {self._offset_minutes}")
    

time_zone1 = TimeZone("ABC", 2, 4)
"""
today = datetime.now(timezone.utc)
print(today) #2024-02-27 22:41:25.575990+00:00
print(today + time_zone1.offset) #2024-02-28 00:45:25.575990+00:00
it added 2 hours and 4 minuntes
"""


