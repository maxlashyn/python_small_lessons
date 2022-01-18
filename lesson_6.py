import click

@click.group('main_group')
def main_group():
    pass

@main_group.command()
@click.option('--name', default = '')
def hello(name):
    print(f"Hello {name}")


@main_group.command()
@click.option('--name', default = '')
@click.option('--file', default = 'test.txt')
def load(name, file):
    with open(file, 'w') as f:
        f.write(f"Hello {name}")


if __name__ == '__main__':
    main_group()