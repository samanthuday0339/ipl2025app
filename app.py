import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="IPL 2025 Dashboard", layout="wide")

# Custom HTML Title
st.markdown("""
    <h1 style='text-align: center; color: #FF5733; font-size: 72px; font-weight: bold;'>IPL 2025</h1>
    <hr style='border: 2px solid #FF5733;'>
""", unsafe_allow_html=True)

pt = pd.read_csv("pointtable.csv")
df = pd.read_csv("IPL2025Batters.csv")
df_bowl = pd.read_csv("IPL2025Bowlers.csv")
continous = ['Runs','Matches', 'Inn', 'BF', 'SR', '100s', '50s', '4s', '6s']
teams = df['Team'].unique()

# Team colors mapping
team_colors = {
    'CSK': '#FEE101',
    'MI': '#045093',
    'RCB': '#DA1818',
    'KKR': '#3A225D',
    'RR': '#EA1A7F',
    'DC': '#17449B',
    'PBKS': '#D71920',
    'SRH': '#FB643E',
    'LSG': '#94C83D',
    'GT': '#0A1C44'
}

# Sidebar Navigation
section = st.sidebar.radio("**🔍 NAVIGATE**", ["Point Table", "Batting", "Bowling"],
                            label_visibility="visible",
                            index=0,
                            help="Choose section to explore")

# -------- POINT TABLE --------
if section == "Point Table":
    st.markdown("""
        <h2 style='color: #0E76A8; font-size:42px; font-weight: bold;'>Point Table</h2>
    """, unsafe_allow_html=True)
    st.dataframe(pt)

# -------- BATTING ANALYSIS --------
elif section == "Batting":
    sub_section = st.sidebar.radio("**Batting Sections**", ["Individual Metrics", "Overall Analysis", "Team Comparisons", "Distributions", "Correlations"] + list(teams))

    if sub_section == "Individual Metrics":
        st.markdown("""
            <h2 style='color: #C70039; font-size:42px; font-weight: bold;'>Top Players - Metric-wise</h2>
        """, unsafe_allow_html=True)
        metrics = ['Runs', '4s', '6s', '50s', '100s', 'BF', 'SR']
        fig, axs = plt.subplots(len(metrics), 1, figsize=(22, 70), constrained_layout=True)
        for i, metric in enumerate(metrics):
            sorted_df = df.sort_values(by=metric, ascending=False)
            sns.barplot(x='Player Name', y=metric, hue='Team', data=sorted_df, dodge=False, ax=axs[i], palette=team_colors)
            axs[i].set_title(f'{metric} by Player')
            axs[i].tick_params(axis='x', rotation=90)
        st.pyplot(fig)

    elif sub_section == "Overall Analysis":
        st.markdown("""
            <h2 style='color: #DAF7A6; font-size:42px; font-weight: bold;'>Overall Scatter Plots</h2>
        """, unsafe_allow_html=True)

        run_types = df.groupby('Team')[['100s', '50s', '4s', '6s','SR']].sum().reset_index()
        run_types = pd.melt(run_types, id_vars='Team', var_name='Score Type', value_name='Count')

        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x='Team', y='Count', hue='Score Type', data=run_types, palette='Set2', ax=ax)
        ax.set_title("COUNT : 100s, 50s, 4s, 6s by Team")
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)

        fig, axs = plt.subplots(9, 1, figsize=(22, 60), constrained_layout=True)
        features = ['Runs', 'Matches', 'Inn', 'No', 'BF', 'SR', '100s', '50s', '6s']
        for i, feat in enumerate(features):
            sns.scatterplot(x=df['Player Name'], y=df[feat], hue=df['Team'], ax=axs[i], palette=team_colors)
            axs[i].set_title(f'{feat} by Players')
            axs[i].tick_params(axis='x', rotation=90)
        st.pyplot(fig)

    elif sub_section == "Team Comparisons":
        st.markdown("""
            <h2 style='color: #FFC300; font-size:42px; font-weight: bold;'>Team-wise Comparison</h2>
        """, unsafe_allow_html=True)

        run_types = df.groupby('Team')[['100s', '50s', '4s', '6s','SR']].sum().reset_index()
        run_types = pd.melt(run_types, id_vars='Team', var_name='Score Type', value_name='Count')

        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x='Team', y='Count', hue='Score Type', data=run_types, palette='Set2', ax=ax)
        ax.set_title("COUNT : 100s, 50s, 4s, 6s by Team")
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)

        for feature in continous:
            data = df.groupby('Team')[feature].sum()
            fig, ax = plt.subplots(figsize=(3.5, 3.5))
            ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90)
            ax.set_title(f"Total {feature} by Team")
            st.pyplot(fig)

    elif sub_section == "Distributions":
        st.markdown("""
            <h2 style='color: #581845; font-size:42px; font-weight: bold;'>Distributions of Player Stats</h2>
        """, unsafe_allow_html=True)
        fig, axs = plt.subplots(7, 1, figsize=(22, 50), constrained_layout=True)
        colors = ['blue', 'red', 'orange', 'green', 'black', 'yellow', 'violet']
        for i, feature in enumerate(['Runs', 'Matches', 'Inn', 'BF', 'SR', '6s', '4s']):
            axs[i].hist(df[feature], bins=20, color=colors[i])
            axs[i].set_title(f'{feature} Distribution')
        st.pyplot(fig)

    elif sub_section == "Correlations":
        st.markdown("""
            <h2 style='color: #900C3F; font-size:42px; font-weight: bold;'>Correlation Heatmap & Pairplot</h2>
        """, unsafe_allow_html=True)
        fig1, ax = plt.subplots(figsize=(6, 4))
        sns.heatmap(df[continous].corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig1)

        st.markdown("""
            <h3 style='color: #FF5733; font-size:34px; font-weight: bold;'>Pairplot</h3>
        """, unsafe_allow_html=True)
        fig2 = sns.pairplot(df[continous], height=1.6)
        st.pyplot(fig2)

    elif sub_section in teams:
        st.markdown(f"""
            <h2 style='color: #117A65; font-size:42px; font-weight: bold;'>{sub_section} - Batting Stats</h2>
        """, unsafe_allow_html=True)
        team_df = df[df['Team'] == sub_section]
        metrics = ['Runs', '4s', '6s', '50s', '100s', 'BF', 'SR']
        fig, axs = plt.subplots(len(metrics), 1, figsize=(22, 70), constrained_layout=True)
        color = team_colors.get(sub_section, '#0A1C44')
        for i, metric in enumerate(metrics):
            sns.barplot(x='Player Name', y=metric, data=team_df, ax=axs[i], color=color)
            axs[i].set_title(f"{metric} - {sub_section}")
            axs[i].tick_params(axis='x', rotation=90)
        st.pyplot(fig)

# -------- BOWLING ANALYSIS --------
elif section == "Bowling":
    sub_bowl = st.sidebar.radio("**Bowling Sections**", ["Individual Metrics", "Overall Analysis", "Team Comparisons"] + list(teams))

    if sub_bowl == "Individual Metrics":
        st.markdown("""
            <h2 style='color: #1F618D; font-size:42px; font-weight: bold;'>Top Bowlers - Metric-wise</h2>
        """, unsafe_allow_html=True)
        metrics = ['WKT', 'MAT', 'INN', 'OVR', 'RUNS', 'ECO', 'SR', 'AVG']
        fig, axs = plt.subplots(len(metrics), 1, figsize=(22, 70), constrained_layout=True)
        for i, metric in enumerate(metrics):
            sorted_df = df_bowl.sort_values(by=metric, ascending=False)
            sns.barplot(x='Player Name', y=metric, hue='Team', data=sorted_df, dodge=False, ax=axs[i], palette=team_colors)
            axs[i].set_title(f'{metric} by Player')
            axs[i].tick_params(axis='x', rotation=90)
        st.pyplot(fig)

    elif sub_bowl == "Overall Analysis":
        st.markdown("""
            <h2 style='color: #148F77; font-size:42px; font-weight: bold;'>Bowling - Overall Analysis</h2>
        """, unsafe_allow_html=True)
        fig, axs = plt.subplots(8, 1, figsize=(22, 60), constrained_layout=True)
        features = ['WKT', 'MAT', 'INN', 'OVR', 'RUNS', 'ECO', 'SR', 'AVG']
        for i, feat in enumerate(features):
            sns.scatterplot(x=df_bowl['Player Name'], y=df_bowl[feat], hue=df_bowl['Team'], ax=axs[i], palette=team_colors)
            axs[i].set_title(f'{feat} by Players')
            axs[i].tick_params(axis='x', rotation=90)
        st.pyplot(fig)

    elif sub_bowl == "Team Comparisons":
        st.markdown("""
            <h2 style='color: #D68910; font-size:42px; font-weight: bold;'>Bowling - Team Comparisons</h2>
        """, unsafe_allow_html=True)
        features = ['WKT', 'MAT', 'INN', 'OVR', 'RUNS']
        summary = df_bowl.groupby('Team')[features].sum().reset_index()
        melted = pd.melt(summary, id_vars='Team', var_name='Metric', value_name='Total')

        fig, ax = plt.subplots(figsize=(14, 6))
        sns.barplot(x='Team', y='Total', hue='Metric', data=melted, palette='Set1', ax=ax)
        ax.set_title("Team-wise Total Bowling Stats")
        st.pyplot(fig)

        for metric in features:
            pie_data = df_bowl.groupby('Team')[metric].sum()
            fig, ax = plt.subplots(figsize=(3.5, 3.5))
            ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
            ax.set_title(f"Team Share - {metric}")
            st.pyplot(fig)

    elif sub_bowl in teams:
        st.markdown(f"""
            <h2 style='color: #196F3D; font-size:42px; font-weight: bold;'>{sub_bowl} - Bowling Stats</h2>
        """, unsafe_allow_html=True)
        team_df = df_bowl[df_bowl['Team'] == sub_bowl]
        metrics = ['WKT', 'MAT', 'INN', 'OVR', 'RUNS', 'ECO', 'SR', 'AVG']
        fig, axs = plt.subplots(len(metrics), 1, figsize=(22, 70), constrained_layout=True)
        color = team_colors.get(sub_bowl, '#0A1C44')
        for i, metric in enumerate(metrics):
            sns.barplot(x='Player Name', y=metric, data=team_df, ax=axs[i], color=color)
            axs[i].set_title(f"{metric} - {sub_bowl}")
            axs[i].tick_params(axis='x', rotation=90)
        st.pyplot(fig)