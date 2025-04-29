import core.module
import core.widget
import requests

class Module(core.module.Module):
    """Shows current XMRig hashrate via the local HTTP API."""

    def __init__(self, config, theme):
        super().__init__(config, theme, core.widget.Widget(self.full_text))
        # HTTP-API settings
        # To learn your token, run `xmrig --http-access-token` in the terminal 
        # or use "ps aux | grep gupax" in a terminal and copy the token
        self._token = "your_token_here"
        self._url   = "http://127.0.0.1:18088/1/summary"

    def full_text(self, widget):
        try:
            headers  = {"Authorization": f"Bearer {self._token}"}
            response = requests.get(self._url, headers=headers, timeout=2)
            data     = response.json()
            hr       = data["hashrate"]["total"][0]  # in H/s
            return f"XMRig: {hr:.0f} H/s"
        except Exception:
            return "XMRig: N/A"
           
