# -*- coding: utf-8 -*-
import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AESCipher(object):
    """
    pip3 install pycryptodome
    """

    def __init__(self, key, mode, **kwargs):
        """
        :param key:
            16 (AES-128)
            24 (AES-192)
            32 (AES-256)
        :param mode: 模式
        :param kwargs:
            iv 初始向量 MODE_CBC 模式使用 必须是16字节

        """
        self.key = key
        self.mode = mode
        self.kwargs = kwargs

    def _get_aes(self):
        """TypeError: decrypt() cannot be called after encrypt()"""
        return AES.new(self.key.encode('utf-8'), self.mode, **self.kwargs)

    def encrypt(self, plain_text):
        # 选择pkcs7补全
        pad_pkcs7 = pad(plain_text.encode('utf-8'), AES.block_size)
        encrypt_data = self._get_aes().encrypt(pad_pkcs7)
        return str(base64.b64encode(encrypt_data), encoding='utf-8')

    def decrypt(self, cipher_text):
        padded_data = self._get_aes().decrypt(base64.b64decode(cipher_text.encode('utf-8')))
        return str(unpad(padded_data, AES.block_size), encoding='utf-8')


def main():
    md5_key = "BGdYBvGedpAdpVHM"
    cipher_text = "IDj5xARMogOh88Z\/yAuFX539gW9\/\/4ZVjSjXmDUUu0BYeDYv0vNHgj3fU7YGROrpSmJMnBxYontO+KUqkt2WHKsuq2gyP+ijHOObDmVm0R7Fwd52RW1izzYwODLFnJeixqHLe1Ai56+Mre3ChxzMIWk973DovQU\/wg4hWvDkRnG95Bfb7O\/XDC3Gg53NE5sKx6LbfP4ufZG0l5mc5Ra287b62AqRQE7E05s+zrerV5een6zx4jzge4w9duQFKDtV5Lod5W1fdXepDzXndvlbNdUxrJyOCPN49l2UdiYIx+SbRo6Juu70f48Ixqm6Hh4wQ1jO1UxIG7mOtvWgaXvQ0gTE79yVwGaugdi3sDo9yz3OXjl2vBgIK3MxvK6A9pmLzCYUKrKNUfM+uQSjznuWaxzYiWv3gVMIywGUsBRqDoEHwf4HH40crPSrG2LBHY14UD6QXgHQT\/TtBnsFr+saReqLlWUAzJEHMYTOeqJNr91NWGN2KBFYcGnOKof3uo+sUwHsgyKXi\/IirrVp+Fq5ljW\/LKjdGRlHt0DVDXGBCUoKnggXPPgLFq20ooKIqwW7CBAlKhsZUVeayRFxGVCQP4oPRPTbr3BYEDCNuTEgYBigB9Ic6BiHQ1bVCvHbUzbybjMascWGYOz7FB4j0DuLAugzyKgWylfSfKQuo\/qE4+wYFZizBPYOgewnYc8LD8g1qc3y0R8UePzCTEq+jHguMkUpfdngVzA38VDvtCULud6nGjn4MuB+zyevGLzYy\/FzBjX8uI9UzeTME77h8qkS1ug55BQpSH2Z9wb5L3ZSzcxOnkh7Pt52JCt9I+ctjlp8K2wCuOAR7a+q+wkkjBPfAoWifm1\/+HrPdB\/2WV8cDAMyrkYQ9g4LAeKeelSK9CD+bjMascWGYOz7FB4j0DuLAlHZG1AqpRka9aa5JsJdsQQYFZizBPYOgewnYc8LD8g1IuTbx4ySvBGifx7CmawNRd4ESBC+9xgSPMVEwcMvcuT+Ff+W9Y3cSCfLwVEPmC2iVsdUHiMF2LQQIe7CYT5DpOg55BQpSH2Z9wb5L3ZSzczRNczLk1JVH1ZZhXuU+dFgW19dAumhAiUmvbds\/5qstPFMPkmBtu7S7WJXgj4I3Gs4OLrj7CDWJWCXiyyodrbpbjMascWGYOz7FB4j0DuLAp1ngcqJ2qc16r32EiKBTor+Ff+W9Y3cSCfLwVEPmC2iw43uzfJHk+0nJwpyc+esPdq5SOeP\/Y0oDglfBmFZzZCDKxxFonL6PqXEahWV8+HjQ9tDAEHJQdQKEHyMCwZ+nOg55BQpSH2Z9wb5L3ZSzcwYiLZ2lUcwuP+vN3igbKST\/j6BJZ4EEnRMMiG0zTc4LymvL7jnSid\/dZfp8k446C38WcIOVMxip3tKOruvTeT2nciLy9edjqGu+H77n\/CoOCmzPx1upTn0yQMm9hTVN8w4\/U+Cqrk7r4SjWUCtavGtbjMascWGYOz7FB4j0DuLAqB7Cy+sBxLMHgpZD25ZersYFZizBPYOgewnYc8LD8g1Y1ZtQm2r2T5Fi493+siC4X8ZfMY8bGYGcvF7ESr7CiZSiQgd+X96cgKZJ2c6aiXbhHvgApWa2axOfVSg73xtRug55BQpSH2Z9wb5L3ZSzcyOipWHjuxKTt3n14uPGkIrNN4cy7FvauFu7DQwM\/uRqymvL7jnSid\/dZfp8k446C31Ga4mvcgs9CTSLbR8i16RqAwrqcDqr+VPnO1mwMArEzTAchyf+5Ve5fsuh5sgItUYFZizBPYOgewnYc8LD8g1pB0ra78tWSVciUSfr9u8Dyd3UZ9Z1djk4xsU\/fnSFD3wvBnO\/wYamT2OH10xhGCILHJdEv0hrPZc0zrD3U+PpSmvL7jnSid\/dZfp8k446C1OmfaBkp919UZbMpqqI5frqAwrqcDqr+VPnO1mwMArE+OvmDA\/AmgIU85EeSd+H6fPXJRxeetu3nRxwPOxyAvabjMascWGYOz7FB4j0DuLAv6dPAxS5InExzdfOHLKWG0YFZizBPYOgewnYc8LD8g1fD4kgLdwV5UBco05Pmv3nPj5jAiQaS1uDkfKLqVh6hf+Ff+W9Y3cSCfLwVEPmC2inBDWSa7JB4mJHoIOJscHhug55BQpSH2Z9wb5L3ZSzcwxlCssatMnin4QqIyPu\/EPvWlnWnfyiFOTe\/aSuaC12YdCesupyFzD5B8Fqr8SRB4rTjP\/x3elHaia0x0\/UzFpqAwrqcDqr+VPnO1mwMArE4HtGY7wd8HnyWlhmc5FLVKew73gvTduwuq746ZMW+tubjMascWGYOz7FB4j0DuLAt1i3o+RgfTlYz+1kObhjIYYFZizBPYOgewnYc8LD8g1CxXkRSWKpX+gpfaDdXGRzusPP576SzPUfB6+K48Pxhj+Ff+W9Y3cSCfLwVEPmC2iarP\/Z8gxMryrEfBiADA53JtTjM2EzcRUCiQKXE9T1TYGj+ZfMPTEOg5kJlHQhzENjcTYjoy6K\/TfeiE9PkQtpymvL7jnSid\/dZfp8k446C2lKjN464Xu+OX6dTD9\/PE8qAwrqcDqr+VPnO1mwMArE61JDAgcZoWpV5LIBTyzFB4lMbzZ3gLMpsFyBotlqPUPbjMascWGYOz7FB4j0DuLAtUFq2CcBUK53C2CGVwUCxUYFZizBPYOgewnYc8LD8g1tYiKdBornoCDheKE3SDWYc5tclov9V7wr0JdBoxPRNP+Ff+W9Y3cSCfLwVEPmC2iUCk1PuTK39r8AQ0GtUBlRQfpJSJXHiG56CVPQQMOSlGYh\/P56TyYcTOFRikZXmkBmIZrSGGMJl8ew1IjKIjBuBbq\/k1q6A57TWrb4L7aS0YGxzJRmIVSfT3XW630DcEJ"

    # ECB 模式
    ecb_cipher = AESCipher(md5_key, mode=AES.MODE_ECB)

    # 7J0VfbEYF0XdLnLuA1b4Fw==
    print(ecb_cipher.decrypt(cipher_text))


if __name__ == '__main__':
    main()
