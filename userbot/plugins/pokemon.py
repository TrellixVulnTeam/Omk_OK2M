#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi

from userbot.utils import admin_cmd

naam = str("Lel")

bot = "@Hexamonbot"

Pokes = "Here Are Your HexaPokes\n➖➖➖➖➖➖➖➖➖➖➖\n\n"


@borg.on(admin_cmd("mypokes$"))
async def _(event):
    if event.fwd_from:
        return
    async with borg.conversation(bot) as conv:
        await conv.send_message("/mypokemon")
        audio = await conv.get_response()
        card = audio.text
        a = card.replace("/display: Level", "")
        b = a.replace("/sort by: Order caught ↑", "")
        c = b.replace("/pagesize: 20", "")
        d = c.replace("/pagesize: 10", "")
        e = d.replace("/pagesize: 15", "")
        f = e.replace("/pagesize: 25", "")
        g = f.replace("/display: IV points", "")
        h = g.replace("/display: EV points", "")
        i = h.replace("/display: Nature", "")
        j = i.replace("/display: Type", "")
        k = j.replace("/display: Type Symbol", "")
        l = k.replace("/display: Catch Rate", "")
        m = l.replace("/display: HP points", "")
        n = m.replace("/display: Attack points", "")
        o = n.replace("/display: Defense points", "")
        p = o.replace("/display: Sp. Attack points", "")
        q = p.replace("/display: Sp defense points", "")
        r = q.replace("/display: Speed points", "")
        s = r.replace("/display: None", "")
        t = s.replace("/display: Total stats points", "")
        u = t.replace("/sort by: Order caught ↓", "")
        v = u.replace("/sort by: Level ↑", "")
        w = v.replace("/sort by: Level ↓", "")
        x = w.replace("/sort by: Pokedex number ↓", "")
        y = x.replace("/sort by: Pokedex number ↑", "")
        z = y.replace("/sort by: IV points ↑", "")
        ab = z.replace("/sort by: IV points ↓", "")
        bc = ab.replace("/sort by: EV points ↓", "")
        cd = bc.replace("/sort by: EV points ↑", "")
        de = cd.replace("/sort by: Name ↑", "")
        ef = de.replace("/sort by: Name ↓", "")
        fg = ef.replace("/sort by: Nature ↑", "")
        gh = fg.replace("/sort by: Nature ↓", "")
        hi = gh.replace("/sort by: Type ↓", "")
        ij = hi.replace("/sort by: Type ↑", "")
        jk = ij.replace("/sort by: Catch Rate ↑", "")
        kl = jk.replace("/sort by: Catch Rate ↓", "")
        lm = kl.replace("/sort by: HP points ↑", "")
        mn = lm.replace("/sort by: HP points ↓", "")
        no = mn.replace("/sort by: Attack points ↓", "")
        op = no.replace("/sort by: Attack points ↑", "")
        pq = op.replace("/sort by: Defense points ↓", "")
        qr = pq.replace("/sort by: Defense points ↑", "")
        rs = qr.replace("/sort by: Sp. Attack points ↑", "")
        st = rs.replace("/sort by: Sp. Attack points ↓", "")
        tu = st.replace("/sort by: Sp defense points ↑", "")
        uv = tu.replace("/sort by: Sp defense points ↓", "")
        vw = uv.replace("/sort by: Speed points ↓", "")
        wx = vw.replace("/sort by: Speed points ↑", "")
        xy = wx.replace("/sort by: Total stats points ↑", "")
        yz = xy.replace("/sort by: Total stats points ↓", "")
        await borg.send_message(event.chat_id, Pokes + yz)


#### MadBoi
#### MadBoi
#### MadBoi
#### MadBoi
