# Copyright (c) 2021 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# Imports
from typing import Any, Union
from bip_utils.addr.atom_addr import AtomAddr
from bip_utils.addr.iaddr_encoder import IAddrEncoder
from bip_utils.ecc import IPublicKey


class AvaxAddrConst:
    """ Class container for Avax address constants. """

    # HRP
    HRP: str = "avax"
    # P-Chain prefix
    PREFIX_P_CHAIN: str = "P-"
    # X-Chain prefix
    PREFIX_X_CHAIN: str = "X-"


class AvaxPChainAddr(IAddrEncoder):
    """ Avax P-Chain address class. It allows the Avax P-Chain address generation. """

    @staticmethod
    def EncodeKey(pub_key: Union[bytes, IPublicKey],
                  **kwargs: Any) -> str:
        """ Get address in Atom format.

        Args:
            pub_key (bytes or IPublicKey): Public key bytes or object
            **kwargs: Not used

        Returns:
            str: Address string

        Raises:
            ValueError: If the public key is not valid
            TypeError: If the public key is not secp256k1
        """
        return AvaxAddrConst.PREFIX_P_CHAIN + AtomAddr.EncodeKey(pub_key,
                                                                 hrp=AvaxAddrConst.HRP)


class AvaxXChainAddr(IAddrEncoder):
    """ Avax X-Chain address class. It allows the Avax X-Chain address generation. """

    @staticmethod
    def EncodeKey(pub_key: Union[bytes, IPublicKey],
                  **kwargs: Any) -> str:
        """ Get address in Atom format.

        Args:
            pub_key (bytes or IPublicKey): Public key bytes or object

        Returns:
            str: Address string

        Raises:
            ValueError: If the public key is not valid
            TypeError: If the public key is not secp256k1
        """
        return AvaxAddrConst.PREFIX_X_CHAIN + AtomAddr.EncodeKey(pub_key,
                                                                 hrp=AvaxAddrConst.HRP)
