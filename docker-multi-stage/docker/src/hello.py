import click 

@click.command()
@click.option('--name', default='', help='Your name')
def say_hello(name):
    click.echo("Hello {}!".format(name))

if __name__ == '__main__':
    say_hello()