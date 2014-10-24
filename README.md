mixcloudpy
==========

A Python wrapper for the [Mixcloud API](http://www.mixcloud.com/developers/).

## Getting Started

All methods are available thorugh the `Mixcloud` class:

```
import mixcloud
mc = mixcloud.Mixcloud()
```

All result sets are Python dictionaries:

```
house_tag = mc.get_tag('house')
house_tag.keys() # [u'url', u'name', u'key']
```

## Users

Get users by *username*:

```
user = mc.get_user('romeroqj')
```

## Tags

Get tags by *slug*:

```
tag = mc.get_tag('house')
```

## Artists

Get artists by *slug*:

```
artist = mc.get_artist('carl-cox')
```

## License

Copyright &copy; 2014 Jorge Romero. Released under The MIT License.

