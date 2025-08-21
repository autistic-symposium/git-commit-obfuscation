## obfuscating your git history for fun, profit, (superficial) privacy, or storytelling

<br>

### how to run

<br>

#### 0. create a new repository in your profile, name it `git-history-story` (or whatever you choose inside `.env`). copy the content of this repo to it.

<br>

#### 1. make sure you have set both username and (primary) email to match your account:

```bash
git config --global user.name neo
git config --global user.email neo@matrix
```

<br>

#### 2. instal deps:

```bash
make install
```

<br>

#### 3. create and configure your `.env` variables:

```bash
cp .env_sample .env
vim .env
```

<br>

#### 4. run [run.py](run.py):

<br>

```bash
make run
```

<br>

----

### troubleshooting

<br>

#### "failed to push some refs"

<br>

```shell
git stash
git push -f origin main
```
