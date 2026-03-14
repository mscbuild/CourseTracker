import click
from database import init_db, add_course, list_courses
from parsers import coursera, udemy

init_db()

@click.group()
def cli():
    """CourseTracker CLI"""
    pass

@cli.command()
@click.option('--platform', default='coursera', help='Platform: coursera or udemy')
@click.option('--query', prompt='Topic', help='Topic to search')
def search(platform, query):
    """Search courses"""
    courses = []
    if platform == 'coursera':
        courses = coursera.search(query)
    elif platform == 'udemy':
        courses = udemy.search(query)
    else:
        click.echo("Platform not supported")
        return

    for c in courses:
        add_course(c['title'], platform, c['url'])
        click.echo(f"Added: {c['title']} ({platform})")

@cli.command()
def list():
    """List saved courses"""
    courses = list_courses()
    for c in courses:
        status = "✅" if c[4] else "❌"
        click.echo(f"{c[0]}. {c[1]} [{c[2]}] {status} - {c[3]}")

if __name__ == "__main__":
    cli()
