from watch import parse

def test_watch():
    assert parse('<iframe width="560" height="315" src="https://open.ac.uk"></iframe>') == None
    assert parse('<iframe src="http://www.youtube.com/embed/IHkH4VQl1v4"></iframe>') == 'https://youtu.be/IHkH4VQl1v4'
    assert parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/IHkH4VQl1v4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == 'https://youtu.be/IHkH4VQl1v4'
