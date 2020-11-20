"""Define the command-line-driven program called scheduler."""

# TODO: import the time object from datetime

# TODO: import the schedule module from the schedule package

import objgraph

# TODO: import the sys and typer packages


def get_size(obj, seen=None):
    """Recursively find the size of a Python object."""
    # Reference:
    # https://goshippo.com/blog/measure-real-size-any-python-object/
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, "__dict__"):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, "__iter__") and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size


def main(depth: int = typer.Option(7)):
    """Construct a schedule and then display it in the console."""
    # TODO: Step 1: create a student's schedule that will contain courses
    student_schedule = schedule.Schedule()
    # TODO: Step 2: create at least courses
    # TODO: Step 3: add the courses to the schedule
    # TODO: Step 4: display the completed schedule
    # TODO: Make sure that you understand how the next three steps work
    # Step 5: display the memory overhead of the schedule
    typer.echo(
        f"Approximate about of memory used to store the schedule: {get_size(student_schedule)} bytes"
    )
    # Step 6: draw a diagram to visualize the contents of the computer's memory
    typer.echo()
    typer.echo("Generating a diagram to show the contents of the computer's memory")
    objgraph.show_refs(
        student_schedule, max_depth=depth, filename="../diagrams/memory-graph.png"
    )
    # Step 7: show the common types stored in the computer's memory
    typer.echo()
    typer.echo("These are the most common types used by the Python program:")
    objgraph.show_most_common_types()
    typer.echo()


if __name__ == "__main__":
    # indirectly call the main function through the typer.run function
    typer.run(main)
