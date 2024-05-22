from domino.testing import piece_dry_run

def test_selenium_web_browser():
    input_data = dict(
        name="test",
        cmd="test",
        stop_on_error="test"
    )
    output_data = piece_dry_run(
        "SeleniumWebBrowserPiece",
        input_data,
    )

    print(output_data)

    assert output_data is not None