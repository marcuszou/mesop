import mesop as me


@me.page(path="/", title="Hello World!",
         security_policy=me.SecurityPolicy(dangerously_disable_trusted_types=True)
         )
def app():
    me.text("Hello World")