Mixcloudpy
==========

A Python wrapper for the [Mixcloud API](http://www.mixcloud.com/developers/).

## Getting Started

All methods are available thorugh the `Mixcloud` class:

```python
import mixcloud
mc = mixcloud.Mixcloud()
```

All result sets are Python dictionaries:

```python
house_tag = mc.get_tag('house')
house_tag.keys() # [u'url', u'name', u'key']
```

## Users

Get users by *username*:

```python
user = mc.get_user('romeroqj')
```

## Tags

Get tags by *slug*:

```python
tag = mc.get_tag('house')
```

Or by *name*:

```python
tag = mc.get_tag('House')
```

## Artists

Get artists by *slug*:

```python
artist = mc.get_artist('carl-cox')
```

Or by *name*:

```python
artist = mc.get_artist('Carl Cox')
```

## Cloudcasts

Cloudcasts belong to users, so the *username* must be passed as argument:

```python
cloudcast = mc.get_cloudcast('spartacus', 'party-time')
```

Cloudcast's identifier can also be a *name*:

```python
cloudcast = mc.get_cloudcast('spartacus', 'Party Time')
```

## Categories

Get categories by *slug*:

```python
category = mc.get_category('tech-house')
```

Or by *name*:

```python
category = mc.get_category('Tech House')
```

## License

Copyright &copy; 2014 Jorge Romero. Released under The MIT License.

