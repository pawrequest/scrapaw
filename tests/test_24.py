import pytest

from scrapaw.pyd import dtg_fnc, dtg_pyd


@pytest.mark.asyncio
async def test_24():
    ep = await dtg_pyd.DTGEpisode.from_url(
        'https://decoding-the-gurus.captivate.fm/episode/hasan-piker-a-swashbuckling-bromance'
    )
    ...


@pytest.mark.asyncio
async def test_25():
    async for res in dtg_fnc.episode_urls_from_url('https://decoding-the-gurus.captivate.fm/'):
        ...


@pytest.mark.asyncio
async def test_podcast():
    pod = dtg_pyd.DTGPodcast()
    async for ep in pod.get_episodes(limit=3):
        assert isinstance(ep, dtg_pyd.DTGEpisode)
    assert pod.episodes
    assert all(isinstance(_, dtg_pyd.DTGEpisode) for _ in pod.episodes)
    assert len(pod.episodes) == 3
    async for ep2 in pod.get_episodes(limit=3):
        assert isinstance(ep2, dtg_pyd.DTGEpisode)
    assert len(pod.episodes) == 6
    async for ep3 in pod.get_episodes(limit=3, max_dupes=3):
        assert isinstance(ep3, dtg_pyd.DTGEpisode)
    assert len(pod.episodes) == 6
