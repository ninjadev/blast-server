from tastypie.serializers import Serializer
from calendar import timegm


class BlastSerializer(Serializer):
    def format_datetime(self, data):
        return timegm(data.utctimetuple())
