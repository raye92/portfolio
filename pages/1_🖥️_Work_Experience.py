import streamlit as st
from utils import show_code

subpages = ["Regression Models", "Model 2"]

def work_page():
    st.set_page_config(page_title = "Work Experience", page_icon = "🖥️")

    subpage = st.sidebar.selectbox("Projects at Data Annotation Tech", subpages)
    if subpage == "Regression Models":
        # st.empty()
        decision_tree()
        show_code(decision_tree)
    elif subpage == "Model 2":
        # st.empty()
        model_2()
        show_code(model_2)


def decision_tree():
    import pandas as pd
    import time
    import matplotlib.pyplot as plt
    from sklearn.tree import DecisionTreeRegressor, plot_tree
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_absolute_error
    from sklearn.model_selection import train_test_split

    st.write("### Melbourne Housing Price Prediction")
    st.markdown("""Two models I worked on at Data Annotation are Decision Tree and Random Forest models.
    These regression models are trained on Melbourne housing data to predict housing prices.
    The models use feature optimization, fitted with leaf node optimization to minimize mean absolute error (MAE).
    """)
    st.write("  \n")
    st.write("##### Actual vs. Predicted Prices")

    # Load and clean data
    data = pd.read_csv("./data/melb_data.csv")
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

    decision_tree = DecisionTreeRegressor(max_leaf_nodes=best_num_nodes) # Could use random_state param
    random_forest = RandomForestRegressor(max_leaf_nodes=800) # Tested and fitted with optimal num

    decision_tree.fit(train_X, train_y)
    random_forest.fit(train_X, train_y)
    tree_preds = decision_tree.predict(val_X).round(0)
    forest_preds = random_forest.predict(val_X).round(0)

    # Display model results
    results_df = pd.DataFrame( {
        'Actual': val_y,
        'DT Prediction': tree_preds,
        'RF Prediction': forest_preds
    })

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()

    total_rows = results_df.shape[0]
    chart = st.line_chart(results_df.iloc[[0,1]], color=["#834cba", "#eb6e21", "#44c2b3"])

    for row in range(1, total_rows):
        chart.add_rows(results_df.iloc[[row-1, row]])
        progress_bar.progress((row+1)/total_rows)
        status_text.text("%i%% Complete" % (((row+1)/total_rows)*100))

        time.sleep(0.05)

    progress_bar.empty()

    st.button("Regenerate")
    st.write("")

    # Display mae
    dt_mae = mean_absolute_error(val_y, tree_preds)
    rf_mae = mean_absolute_error(val_y, forest_preds)
    st.write("Decision Tree Mean Absolute Error: $", dt_mae)
    st.write("Random Forrest MAE: $", rf_mae)
    st.write("We can see the use of multiple tree components generally results in a more accurate result.")
    st.write("")

    # Display data
    st.write("Model Vs. Actual Housing Prices: ")
    st.dataframe(results_df.T)
    st.write("Feature Values: ")
    st.dataframe(val_X.T, height = 200)
    st.write("Original Melbourne Housing Data (Before preprocessing, cleaning, and feature engineering): ")
    st.dataframe(data, height = 150)

    # Sample tree diagram
    st.write("  \n #### Simplified Tree Model:")
    sample_model = DecisionTreeRegressor(max_leaf_nodes=6, random_state=0)
    sample_model.fit(X, y)
    fig, ax = plt.subplots(figsize=(20,8))
    plot_tree(sample_model, filled=True, feature_names=features, ax=ax)
    st.pyplot(fig)
    st.write("""
    This plot illustrates a simplified version of the decision tree regressor trained on Melbourne's Housing data.
    Each node in the tree presents two paths to traverse based on a feature inequality, and the subsequent nodes indicate the predicted price.
    Features of the seleteced test data is shown above.
    """)


def model_2():
    st.title("Model 2")


if __name__ == "__main__":
    work_page()
