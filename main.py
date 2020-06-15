import kivy
import boto3
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.app import App

Builder.load_string('''
<HelloWorldScreen>:
    cols: 1
    Label:
        text: 'Buckets %s' % root.buckets
    Button:
        text: 'Click me! %d' % root.counter
        on_release: root.my_callback()
''')

class HelloWorldScreen(GridLayout):
    counter = NumericProperty(0)
    buckets = "1"
    def my_callback(self):
        client = boto3.client('s3',
            aws_access_key_id='*****',
            aws_secret_access_key='*******',
            aws_session_token='******',
        )
        response = client.list_buckets()
        #print(response)
        self.buckets = response
        #for bucket in response['Buckets']:
            #print(f'  {bucket["Name"]}')
        print(buckets.length)
        self.counter += 1

class HelloWorldApp(App):
    def build(self):
        return HelloWorldScreen()

if __name__ == '__main__':
    HelloWorldApp().run()
