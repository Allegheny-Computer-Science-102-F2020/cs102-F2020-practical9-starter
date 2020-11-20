"""Represent the schedule for a student's courses at Allegheny College."""

# TODO: import the OrderedDict object from collections

# TODO: import the time object from datetime


class Course:
    """Define a Course class."""

    def __init__(self, title: str, start: time, end: time, instructor: str) -> None:
        """Define the constructor for a course."""
        # TODO: Provide the complete constructor for this object

    def __repr__(self) -> str:
        """Return a textual representation of the course."""
        return f"{self.title} that starts at {self.start} and ends at {self.end} and is taught by {self.instructor}"


class Schedule:
    """Define a Schedule that contains zero to many Course objects."""

    def __init__(self) -> None:
        """Create an empty schedule."""
        # TODO: Provide the complete constructor for this object

    def add(self, course: Course, day: str) -> None:
        """Add a new course to the schedule on the given day of the week."""
        # if the day is not in the dictionary representing the
        # schedule, then create an empty list and add it
        if day not in self.schedule:
            day_list = []
            day_list.append(course)
            self.schedule[day] = day_list
        # if the day is already in the dictionary that represents the
        # schedule, then append the current course to the list
        # note that you do not need to re-assign the list to the
        # value in the dictionary because of the fact that the list
        # is stored as a reference which is updated through append
        else:
            current_day_list = self.schedule[day]
            current_day_list.append(course)

    def __repr__(self) -> str:
        """Return a textual representation of a course schedule."""
        # start the textual representation off with a newline
        weekly_schedule = "\n"
        # iterate through each day of the week in the schedule
        for day in self.schedule.keys():
            # add the name of the current day of the week
            weekly_schedule += day + ":\n\n\t"
            # access the schedule for the current day of the week
            schedule_for_day = self.schedule[day]
            # add all of the classes of the current day of the week
            weekly_schedule += "\n\t".join(map(str, schedule_for_day))
            # for course in schedule_for_day:
            # weekly_schedule += str(course) + "\n"
            # if not processing the last day of the week, add two newlines
            if day != list(self.schedule.keys())[-1]:
                weekly_schedule += "\n\n"
            # if processing the last day of the week, add one newline
            else:
                weekly_schedule += "\n"
        # return a string that displays all courses taught in a week
        return weekly_schedule
