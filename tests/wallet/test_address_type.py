from typing import Any, Dict

import pytest

from maize.wallet.util.address_type import AddressType, ensure_valid_address, is_valid_address


@pytest.mark.parametrize("prefix", [None])
def test_xmz_hrp_for_default_config(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    assert AddressType.XMZ.hrp(config) == "xmz"


@pytest.mark.parametrize("prefix", ["txmz"])
def test_txmz_hrp_for_testnet(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    assert AddressType.XMZ.hrp(config) == "txmz"


@pytest.mark.parametrize("prefix", [None])
def test_is_valid_address_xmz(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    valid = is_valid_address(
        "xmz1mnr0ygu7lvmk3nfgzmncfk39fwu0dv933yrcv97nd6pmrt7fzmhs8taffd", allowed_types={AddressType.XMZ}, config=config
    )
    assert valid is True


@pytest.mark.parametrize("prefix", ["txmz"])
def test_is_valid_address_txmz(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    # TXMZ address validation requires a config
    valid = is_valid_address(
        "txmz1mnr0ygu7lvmk3nfgzmncfk39fwu0dv933yrcv97nd6pmrt7fzmhs2v6lg7",
        allowed_types={AddressType.XMZ},
        config=config,
    )
    assert valid is True


@pytest.mark.parametrize("prefix", [None])
def test_is_valid_address_xmz_bad_address(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    valid = is_valid_address(
        "xmz1mnr0ygu7lvmk3nfgzmncfk39fwu0dv933yrcv97nd6pmrt7fzmhs8xxxxx", allowed_types={AddressType.XMZ}, config=config
    )
    assert valid is False


@pytest.mark.parametrize("prefix", [None])
def test_is_valid_address_nft(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    valid = is_valid_address(
        "nft1mx2nkvml2eekjtqwdmxvmf3js8g083hpszzhkhtwvhcss8efqzhqtza773", allowed_types={AddressType.NFT}, config=config
    )
    assert valid is True


@pytest.mark.parametrize("prefix", ["txmz"])
def test_is_valid_address_nft_with_testnet(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    valid = is_valid_address(
        "nft1mx2nkvml2eekjtqwdmxvmf3js8g083hpszzhkhtwvhcss8efqzhqtza773", allowed_types={AddressType.NFT}, config=config
    )
    assert valid is True


@pytest.mark.parametrize("prefix", [None])
def test_is_valid_address_nft_bad_address(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    valid = is_valid_address(
        "nft1mx2nkvml2eekjtqwdmxvmf3js8g083hpszzhkhtwvhcss8efqzhqtxxxxx", allowed_types={AddressType.NFT}, config=config
    )
    assert valid is False


@pytest.mark.parametrize("prefix", [None])
def test_is_valid_address_did(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    valid = is_valid_address(
        "did:maize:14jxdtqcyp3gk8ka0678eq8mmtnktgpmp2vuqq3vtsl2e5qr7fyrsr9gsr7",
        allowed_types={AddressType.DID},
        config=config,
    )
    assert valid is True


@pytest.mark.parametrize("prefix", ["txmz"])
def test_is_valid_address_did_with_testnet(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    valid = is_valid_address(
        "did:maize:14jxdtqcyp3gk8ka0678eq8mmtnktgpmp2vuqq3vtsl2e5qr7fyrsr9gsr7",
        allowed_types={AddressType.DID},
        config=config,
    )
    assert valid is True


@pytest.mark.parametrize("prefix", [None])
def test_is_valid_address_did_bad_address(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    valid = is_valid_address(
        "did:maize:14jxdtqcyp3gk8ka0678eq8mmtnktgpmp2vuqq3vtsl2e5qr7fyrsrxxxxx",
        allowed_types={AddressType.DID},
        config=config,
    )
    assert valid is False


@pytest.mark.parametrize("prefix", [None])
def test_ensure_valid_address_xmz(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    address = ensure_valid_address(
        "xmz1mnr0ygu7lvmk3nfgzmncfk39fwu0dv933yrcv97nd6pmrt7fzmhs8taffd", allowed_types={AddressType.XMZ}, config=config
    )
    assert address == "xmz1mnr0ygu7lvmk3nfgzmncfk39fwu0dv933yrcv97nd6pmrt7fzmhs8taffd"


@pytest.mark.parametrize("prefix", ["txmz"])
def test_ensure_valid_address_txmz(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    address = ensure_valid_address(
        "txmz1mnr0ygu7lvmk3nfgzmncfk39fwu0dv933yrcv97nd6pmrt7fzmhs2v6lg7",
        allowed_types={AddressType.XMZ},
        config=config,
    )
    assert address == "txmz1mnr0ygu7lvmk3nfgzmncfk39fwu0dv933yrcv97nd6pmrt7fzmhs2v6lg7"


@pytest.mark.parametrize("prefix", [None])
def test_ensure_valid_address_xmz_bad_address(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    with pytest.raises(ValueError):
        ensure_valid_address(
            "xmz1mnr0ygu7lvmk3nfgzmncfk39fwu0dv933yrcv97nd6pmrt7fzmhs8xxxxx",
            allowed_types={AddressType.XMZ},
            config=config,
        )


@pytest.mark.parametrize("prefix", [None])
def test_ensure_valid_address_nft(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    address = ensure_valid_address(
        "nft1mx2nkvml2eekjtqwdmxvmf3js8g083hpszzhkhtwvhcss8efqzhqtza773", allowed_types={AddressType.NFT}, config=config
    )
    assert address == "nft1mx2nkvml2eekjtqwdmxvmf3js8g083hpszzhkhtwvhcss8efqzhqtza773"


@pytest.mark.parametrize("prefix", [None])
def test_ensure_valid_address_nft_bad_address(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    with pytest.raises(ValueError):
        ensure_valid_address(
            "nft1mx2nkvml2eekjtqwdmxvmf3js8g083hpszzhkhtwvhcss8efqzhqtxxxxx",
            allowed_types={AddressType.NFT},
            config=config,
        )


@pytest.mark.parametrize("prefix", [None])
def test_ensure_valid_address_did(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    address = ensure_valid_address(
        "did:maize:14jxdtqcyp3gk8ka0678eq8mmtnktgpmp2vuqq3vtsl2e5qr7fyrsr9gsr7",
        allowed_types={AddressType.DID},
        config=config,
    )
    assert address == "did:maize:14jxdtqcyp3gk8ka0678eq8mmtnktgpmp2vuqq3vtsl2e5qr7fyrsr9gsr7"


@pytest.mark.parametrize("prefix", [None])
def test_ensure_valid_address_did_bad_address(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    with pytest.raises(ValueError):
        ensure_valid_address(
            "did:maize:14jxdtqcyp3gk8ka0678eq8mmtnktgpmp2vuqq3vtsl2e5qr7fyrsrxxxxx",
            allowed_types={AddressType.DID},
            config=config,
        )


@pytest.mark.parametrize("prefix", [None])
def test_ensure_valid_address_bad_length(config_with_address_prefix: Dict[str, Any]) -> None:
    config = config_with_address_prefix
    with pytest.raises(ValueError):
        ensure_valid_address("xmz1qqqqqqqqqqqqqqqqwygzk5", allowed_types={AddressType.XMZ}, config=config)
