def send(self, topic_name, key,value, headers = None):
    self.validatePayload(topic_name, key, value)
    
    try:
        jsonValue = json.dumps(value.__dict__)
    except:
        raise KafkaSerializationException("Invalid class object sent. Please send a class. \n {}".format(err))
    
    self.json_producer.produce(topic = topic_name, key = key, value = jsonValue, headers = headers, on_delivery = (lambda err, msg: self.delivery_report(err,msg)))
    
    self.json_producer.flush()
    if self.err is None:
        traceId = None
        if headers is not None:
            if type(headers) is dict:
                traceId = headers.get('traceId', None)
            if traceId is not None:
                logging.info('TraceId: {} | Message sent to topic {}'.format(traceId, topic_name))
            return self.topic_partition
        else:
            raise KafkaProducerException(error = self.err, message = self.err.str())