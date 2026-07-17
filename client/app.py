import asyncio
import json

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.json import JSON

from .session import MCPConnection
from .router import MCPRouter

console = Console()


def display_result(result):

    if result.is_error:
        console.print(Panel(result.content[0].text, title="Error", border_style="red"))
        return

    data = result.data

    # FastMCP sometimes returns JSON as text content
    if data is None and result.content:

        text = result.content[0].text

        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            console.print(text)
            return

    if isinstance(data, list):

        if not data:
            console.print(Panel("No records found", border_style="yellow"))
            return

        if isinstance(data[0], dict):

            table = Table(header_style="bold cyan", show_lines=True)

            for column in data[0].keys():
                table.add_column(column.capitalize())

            for row in data:
                table.add_row(*[str(value) for value in row.values()])

            console.print(table)

    elif isinstance(data, dict):

        table = Table(show_header=False)

        for key, value in data.items():
            table.add_row(key.capitalize(), str(value))

        console.print(Panel(table, title="Employee", border_style="green"))

    else:
        console.print(data)


async def invoke_tool(client, tool):

    args = {}

    if tool.name == "get_employee":
        employee_id = console.input("Employee ID: ")
        args["employee_id"] = int(employee_id)

    elif tool.name == "search_employees":
        query = console.input("Search name: ")
        args["query"] = query

    elif tool.name == "search_documents":
        query = console.input("Search document: ")
        args["query"] = query

    result = await client.call_tool(tool.name, args)
    console.print("\n[bold green]Result:[/bold green]\n")

    display_result(result)


async def main():

    document_client = MCPConnection("python", ["-m", "document_server.app"])
    employee_client = MCPConnection("python", ["-m", "employee_server.app"])

    await document_client.connect()
    await employee_client.connect()

    router = MCPRouter()
    router.register("documents", document_client)
    router.register("employees", employee_client)

    while True:

        console.print("\n[bold cyan]========== MCP Client ==========[/bold cyan]")

        console.print("1. Documents")
        console.print("2. Employees")
        console.print("0. Exit")

        choice = console.input("\nSelect server: ")

        if choice == "0":
            break

        if choice == "1":
            server = "documents"

        elif choice == "2":
            server = "employees"

        else:
            console.print("[red]Invalid option[/red]")
            continue

        client = router.routes[server]
        tools = await client.tools()
        console.print(f"\n[bold]{server.capitalize()} tools[/bold]")

        for index, tool in enumerate(tools, start=1):
            console.print(f"{index}. {tool.name}")

        selected = int(console.input("\nSelect tool: "))
        tool = tools[selected - 1]

        await invoke_tool(client, tool)

    await document_client.close()
    await employee_client.close()


if __name__ == "__main__":
    asyncio.run(main())
