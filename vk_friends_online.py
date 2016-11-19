import vk
import argparse

APP_ID = 5669032


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_online = api.friends.getOnline()
    return api.users.get(user_ids=friends_online, fields=['first_name', 'last_name'])


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--login', help="Your login", required=True)
    parser.add_argument(
        '-p', '--password', help="Your password", required=True)

    args = parser.parse_args()

    friends_online = get_online_friends(args.login, args.password)
    output_friends_to_console(friends_online)
