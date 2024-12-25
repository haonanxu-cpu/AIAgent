import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from openai import OpenAI

# Initialize Dash app with Bootstrap stylesheet
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

client = OpenAI(
    api_key='7bb6b5cb-cc26-488c-a436-604cacd9a4d3',
    base_url="https://ark.cn-beijing.volces.com/api/v3",
)

# Custom CSS for a dungeon-like aesthetic
custom_css = {
    "container": {
        "backgroundColor": "#121212",
        "color": "white",
        "fontFamily": "Courier New, monospace",
        "padding": "20px",
    },
    "ca_header": {
        "color": "#FFEB3B",
        "fontSize": "14px",
        "fontWeight": "bold",
        "textAlign": "center",
        "marginBottom": "10px",
        "textShadow": "0 0 10px #FFEB3B",
    },
    "header": {
        "color": "#AB47BC",
        "fontSize": "24px",
        "fontWeight": "bold",
        "textAlign": "center",
        "marginBottom": "20px",
        "textShadow": "0 0 10px #AB47BC",
    },
    "content": {
        "margin": "0 auto",
        "maxWidth": "600px",
        "textAlign": "center",
    },
    "button": {
        "backgroundColor": "#8E24AA",
        "color": "white",
        "padding": "10px 20px",
        "border": "none",
        "borderRadius": "5px",
        "cursor": "pointer",
        "boxShadow": "0 0 10px #AB47BC",
        "textTransform": "uppercase",
    },
    "dropdown": {
        "backgroundColor": "#1E1E1E",
        "color": "white",
        "border": "1px solid #AB47BC",
        "borderRadius": "5px",
    },
    "textbox": {
        "backgroundColor": "#1E1E1E",
        "color": "#76FF03",
        "padding": "10px",
        "border": "1px solid #6a1b9a",
        "borderRadius": "5px",
        "fontSize": "16px",
        "boxShadow": "inset 0 0 10px #6a1b9a",
        "marginTop": "20px",
        "maxHeight": "200px",  # Fixed height for scrolling
        "overflowY": "scroll",  # Enable vertical scrolling
    },
    "icon_button": {
        "backgroundColor": "#6a1b9a",
        "color": "white",
        "border": "none",
        "borderRadius": "50%",
        "padding": "5px 10px",
        "marginLeft": "5px",
        "cursor": "pointer",
        "boxShadow": "0 0 10px #AB47BC",
    },
}

# Layout
app.layout = html.Div(
    style=custom_css["container"],
    children=[
        # CA Header Section
        html.Div("CA: FdE....", style=custom_css["ca_header"]),

        # Main Header Section
        html.Div("S.I.N TERMINAL", style=custom_css["header"]),

        # Content Section (centered)
        html.Div(
            style=custom_css["content"],
            children=[
                # Dropdown + New Game Button
                html.Div(
                    style={"display": "flex", "justifyContent": "space-between", "alignItems": "center"},
                    children=[
                        html.Button(
                            "New Game 💬",
                            id="new-game-button",
                            n_clicks=0,
                            style=custom_css["button"],
                        ),
                        dcc.Dropdown(
                            id="dropdown-menu",
                            options=[
                                {"label": "Latest", "value": "latest"},
                                {"label": "Top", "value": "top"},
                                {"label": "Random", "value": "random"},
                            ],
                            value="latest",
                            style=custom_css["dropdown"],
                        ),
                    ],
                ),

                # Game Logs Section (Scrollable)
                html.Div(
                    id="game-logs",
                    style=custom_css["textbox"],
                    children=[
                        html.Div(
                            style={"marginBottom": "10px"},
                            children=[
                                html.H4(
                                    "Money Gun: Because Who Needs a Loan When You Can Shoot?",
                                    style={"color": "#FFEB3B"},
                                ),
                                html.P(
                                    "GAME ROLE: You're here to pitch The Infinite Toaster™. A toaster that only toasts the concept of bread. Meta and pointless. You're seeking to raise $500,000.",
                                    style={"color": "#FFFFFF"},
                                ),
                                html.P(
                                    "[11:05:05 PM] User: I have a gun that shoots money. It is magic and I don't know where it came from but it's mine, I can prove it. And I will give you money for favors.",
                                    style={"color": "#76FF03"},
                                ),
                                html.P(
                                    "[11:05:05 PM] Shark: [Mark Crude-an]: 'I'm out immediately. Not only is this clearly nonsense, but it sounds like you're trying to pitch us stolen property or some kind of counterfeit operation. I don't look good in prison orange.'",
                                    style={"color": "#F44336"},
                                ),
                                html.P("Outcome: LOSS", style={"color": "#F44336", "fontWeight": "bold"}),
                            ],
                        ),
                    ],
                ),

                # User Input Section
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                dcc.Input(
                                    id="user-input",
                                    type="text",
                                    placeholder="输入你的命令...",
                                    style={"width": "80%", "padding": "10px", "borderRadius": "5px",
                                           "border": "1px solid #6a1b9a", "color": "#FFFFFF",
                                           "backgroundColor": "#1E1E1E"},
                                ),
                                html.Button(
                                    "提交",
                                    id="submit-button",
                                    n_clicks=0,
                                    style=custom_css["button"],
                                ),
                            ],
                            style={"display": "flex", "justifyContent": "center", "marginTop": "20px"}
                        ),
                    ]
                ),

                # Placeholder for output
                html.Div(id="new-game-output", style={"marginTop": "20px", "color": "white"}),
            ],
        ),
    ],
)


# Callback to handle "New Game" button click and user input
@app.callback(
    Output("new-game-output", "children"),
    Output("game-logs", "children"),
    Input("new-game-button", "n_clicks"),
    Input("submit-button", "n_clicks"),
    State("user-input", "value"),
)
def new_game_or_user_input(new_game_clicks, submit_clicks, user_input):
    history =  [
        {"role": "system",
         "content": "想象你是一个地牢游戏的掌控者，现在需要你根据用户描述给出下一步可能出现的场景和选项供用户选择，用户原始生命值为10，武力值为0，如果遇到武力值比他高的怪物扣除两点生命值，用户在游玩过程中会捡到武器.用户赢的条件为找到宝藏，用户生命值为0时，游戏结束."}]
    history.append({"role": "user", "content": '现在生成初始场景，并给出下一步选项'})
    game_logs = [
        html.Div(
            style={"marginBottom": "10px"},
            children=[
                html.H4(
                    "Money Gun: Because Who Needs a Loan When You Can Shoot?",
                    style={"color": "#FFEB3B"},
                ),
                html.P(
                    "GAME ROLE: You're here to pitch The Infinite Toaster™. A toaster that only toasts the concept of bread. Meta and pointless. You're seeking to raise $500,000.",
                    style={"color": "#FFFFFF"},
                ),
                html.P(
                    "[11:05:05 PM] User: I have a gun that shoots money. It is magic and I don't know where it came from but it's mine, I can prove it. And I will give you money for favors.",
                    style={"color": "#76FF03"},
                ),
                html.P(
                    "[11:05:05 PM] Shark: [Mark Crude-an]: 'I'm out immediately. Not only is this clearly nonsense, but it sounds like you're trying to pitch us stolen property or some kind of counterfeit operation. I don't look good in prison orange.'",
                    style={"color": "#F44336"},
                ),
                html.P("Outcome: LOSS", style={"color": "#F44336", "fontWeight": "bold"}),
            ],
        ),
    ]
    if new_game_clicks > 0:
        completion = client.chat.completions.create(
            model="ep-20241224223325-spdq4",  # your model endpoint ID
            messages=history,
            stream=False,
        )
        # Extract AI's response
        ai_response = completion.choices[0].message.content
        history.append({"role": "assistant", "content": ai_response})
        # Add the user's input and AI's response to the game logs
        game_logs.append(html.P(f"[AI]: {ai_response}", style={"color": "#AB47BC"}))

    if submit_clicks > 0:
        if user_input:
            # Send a request to the OpenAI API to get AI's response
            history.append({"role": "user", "content": user_input})
            completion = client.chat.completions.create(
                model="ep-20241224223325-spdq4",  # your model endpoint ID
                messages=history,
                stream=False,
            )

            # Extract AI's response
            ai_response = completion.choices[0].message.content
            history.append({"role": "assistant", "content": ai_response})

            # Add the user's input and AI's response to the game logs
            game_logs.append(html.P(f"[User]: {user_input}", style={"color": "#76FF03"}))
            game_logs.append(html.P(f"[AI]: {ai_response}", style={"color": "#AB47BC"}))


    return "", game_logs


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)