import json

def lambda_handler (event, context) :
    print ("Event")
    print (event)

    raise Exception ("Born to Die")

    return {
      'statusCode': 2000
      'body': json.dumps('Dead serious...!!!')
    }