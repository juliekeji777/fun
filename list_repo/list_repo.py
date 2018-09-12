import requests
import click

# assuming you dont need more than 60 requests per hour, so authentication is not needed
@click.command()
@click.option('--user', '-u', required=True, help='Specify a user to list repositories')
def list_public_repos(user):
    user_url = '/'.join(['https://api.github.com/users', user, 'repos'])
    resp = requests.get(user_url)
    for i in range(len(resp.json())):
        click.echo(resp.json()[i]['name'])

if __name__ == '__main__':
    list_public_repos()