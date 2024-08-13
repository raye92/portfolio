import streamlit as st
from utils import show_code

subpages = ["Decision Tree", "Model 2"]

def work_page():
    st.set_page_config(page_title = "Work Experience", page_icon = "🖥️")

    st.write("## Projects at Data Annotation Tech")
    st.write("### Melbourne Housing Price Prediction with Decision Trees")
    st.markdown("""This Decision Tree Regression model is trained on Melbourne housing data to predict housing prices.
    The model uses feature optimization, tuned with leaf node sizes to minimize Mean Absolute Error.
    The predictions and actual values are graphed below:
    """)
    st.write("##### Actual vs. Predicted Melbourne Housing Prices")

    subpage = st.sidebar.selectbox("Projects", subpages)
    if subpage == "Decision Tree":
        decision_tree()
        show_code(decision_tree)
    elif subpage == "Model 2":
        model_2()
        show_code(model_2)

def decision_tree():
    import pandas as pd
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.metrics import mean_absolute_error
    from sklearn.model_selection import train_test_split
    import time

    # Load and clean data
    data = pd.read_csv("melb_data.csv")
    data = data.dropna(axis=0)

    # Choose target and features, features optimized
    y = data.Price
    features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude', 'BuildingArea', 'YearBuilt', 'Propertycount']
    X = data[features]

    train_X, val_X, train_y, val_y = train_test_split(X, y, test_size=0.01) #1% test size, Could use random_state param

    # Fitting model with max_leaf_nodes
    def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
        model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
        model.fit(train_X, train_y)
        prediction=model.predict(val_X)
        mae = mean_absolute_error(val_y, prediction)
        return(mae)

    max_leaf_nodes = [5, 25, 50, 100, 250, 500]
    maes = {max_leaf_node: get_mae(max_leaf_node, train_X, val_X, train_y, val_y) for max_leaf_node in max_leaf_nodes}
    best_num_nodes = min(maes, key=maes.get)

    melb_model = DecisionTreeRegressor(max_leaf_nodes=best_num_nodes) # Could use random_state param
    melb_model.fit(train_X, train_y)
    predictions = melb_model.predict(val_X).round(0)

    # Display model results
    results_df = pd.DataFrame( {
        'Actual': val_y,
        'Prediction': predictions
    })

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()

    total_rows = results_df.shape[0]
    chart = st.line_chart(results_df.iloc[[0,1]], color=["#834cba", "#eb6e21"])

    for row in range(1, total_rows):
        chart.add_rows(results_df.iloc[[row-1, row]])
        progress_bar.progress((row+1)/total_rows)
        status_text.text("%i%% Complete" % (((row+1)/total_rows)*100))

        time.sleep(0.05)

    # Display mae
    mae = mean_absolute_error(val_y, predictions)
    st.write("Mean Absolute Error: $", mae)

    # Display data
    st.write("Model Vs. Actual Housing Prices")
    st.dataframe(results_df.T)
    st.write("Feature Values")
    st.dataframe(val_X.T, height = 200)


def model_2():
    st.title("Model 2")


if __name__ == "__main__":
    work_page()
