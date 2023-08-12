# slackscrape
Tutorial to get your API token:

https://www.loom.com/share/e155a004f0ef49a2bc2dd7348a06036d



## Usage

Add your [slack token](https://api.slack.com/docs/oauth-test-tokens) credentials to `getMemberInfo.py` in project and the project root under env.json

eg:

```js
  sc = WebClient(
        token="xoxb-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

```
env.json
```js
{
  "token": "xxxxxx-XXXXXXXX-XXXXXXXX-xxxxxxxx"
}
```

## Get all info on the users in the slack workspace

`python getMemberInfo.py`

the following info will be extracted and saved to a csv
Real Name	|   Email	|  Phone	|   Channels



These are additional functionalities:

## slackscrape

`python slackscrape.py -c [channel id]`

eg: `python slackscrape.py -c C193MSB9J

will write channel messages to `general.json` in `output/channels/general/messages/`

## get channels messages

`python get\_channels\_messages.py -u [optional update existing] -a [optional include archived]`

eg: `python get\_channels\_messages.py -u

Will get all channels messages and update with any new messages it finds and write to
`output/channels/<channel>/messages/<channel>.json`

## get channels info

`python get\_channels\_info.py -u [optional update existing]`

eg: `python get\_channels\_info.py -u

Will get all channels metadata and write to
`output/channels/<channel>/info/<channel>.json`

## get users

`python get\_users.py -u [optional update existing]`

eg: `python get\_users.py -u

Will get all users and write to `output/users/members/<user>.json`

## count emojis

`python count_emojis.py`

Extracts all messages from all chanenls and does a team-wide breakdown of the top 50 most popular emojis & reactions.

## Dependencies

```bash
pip install slackclient
```
