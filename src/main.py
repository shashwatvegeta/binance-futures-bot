import typer
from typing import Optional
from src.market_orders import place_market_order
from src.limit_orders import place_limit_order
from src.advanced.stop_limit import place_stop_limit_order
from src.logger import logger

app = typer.Typer()

@app.command()
def market(symbol: str, side: str, quantity: float):
    """
    Place a Market Order.
    Example: python src/main.py market BTCUSDT BUY 0.001
    """
    if quantity <= 0:
        typer.echo("Error: Quantity must be positive.")
        return
    if side.upper() not in ['BUY', 'SELL']:
        typer.echo("Error: Side must be BUY or SELL.")
        return

    place_market_order(symbol.upper(), side.upper(), quantity)

@app.command()
def limit(symbol: str, side: str, quantity: float, price: float):
    """
    Place a Limit Order.
    Example: python src/main.py limit BTCUSDT SELL 0.001 50000
    """
    if quantity <= 0:
        typer.echo("Error: Quantity must be positive.")
        return
    if price <= 0:
        typer.echo("Error: Price must be positive.")
        return
    if side.upper() not in ['BUY', 'SELL']:
        typer.echo("Error: Side must be BUY or SELL.")
        return

    place_limit_order(symbol.upper(), side.upper(), quantity, price)

@app.command()
def stop_limit(symbol: str, side: str, quantity: float, price: float, stop_price: float):
    """
    Place a Stop-Limit Order.
    Example: python src/main.py stop-limit BTCUSDT SELL 0.001 49000 49500
    """
    if quantity <= 0:
        typer.echo("Error: Quantity must be positive.")
        return
    if price <= 0 or stop_price <= 0:
        typer.echo("Error: Price and Stop Price must be positive.")
        return
    if side.upper() not in ['BUY', 'SELL']:
        typer.echo("Error: Side must be BUY or SELL.")
        return

    place_stop_limit_order(symbol.upper(), side.upper(), quantity, price, stop_price)

if __name__ == "__main__":
    app()
