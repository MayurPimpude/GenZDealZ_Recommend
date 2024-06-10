import pandas as pd

def data():
# Provided data
    data = [
        {'user': 'user1', 'purchases': ['amazon', 'flipkart', 'myntra']},
        {'user': 'user2', 'purchases': ['amazon', 'flipkart', 'mcd']},
        {'user': 'user3', 'purchases': ['dominos', 'kfc', 'swiggy', 'maxfashion']},
        {'user': 'user4', 'purchases': ['myntra', 'nykaa', 'pvr']},
        {'user': 'user5', 'purchases': ['mcd', 'kfc', 'pizzahut']},
        {'user': 'user6', 'purchases': ['zee5', 'pvr', 'prime', 'reliancesmart']},
        {'user': 'user7', 'purchases': ['nykaa', 'wildcraft']},
        {'user': 'user8', 'purchases': ['croma', 'vijaysales', 'flipkart']},
        {'user': 'user9', 'purchases': ['uber', 'ola', 'blinkit']},
        {'user': 'user10', 'purchases': ['swiggy', 'dominos']},
        {'user': 'user11', 'purchases': ['amazon', 'myntra', 'nykaa', 'wildcraft', 'mcd']},
        {'user': 'user12', 'purchases': ['puma', 'maxfashion', 'croma']},
        {'user': 'user13', 'purchases': ['vijaysales', 'amazon', 'reliancesmart']},
        {'user': 'user14', 'purchases': ['pvr', 'zee5']},
        {'user': 'user15', 'purchases': ['ola', 'uber', 'blinkit', 'pizzahut']},
        {'user': 'user16', 'purchases': ['flipkart', 'myntra', 'nykaa']},
        {'user': 'user17', 'purchases': ['maxfashion', 'puma']},
        {'user': 'user18', 'purchases': ['dominos', 'kfc', 'mcd', 'swiggy']},
        {'user': 'user19', 'purchases': ['croma', 'vijaysales', 'reliancesmart']},
        {'user': 'user20', 'purchases': ['zee5', 'pvr', 'prime']},
        {'user': 'user21', 'purchases': ['amazon', 'flipkart', 'myntra']},
        {'user': 'user22', 'purchases': ['flipkart', 'mcd']},
        {'user': 'user23', 'purchases': ['dominos', 'kfc', 'swiggy', 'maxfashion']},
        {'user': 'user24', 'purchases': ['myntra', 'nykaa', 'pvr']},
        {'user': 'user25', 'purchases': ['mcd', 'kfc', 'pizzahut']},
        {'user': 'user26', 'purchases': ['zee5', 'pvr', 'prime', 'reliancesmart']},
        {'user': 'user27', 'purchases': ['nykaa', 'wildcraft']},
        {'user': 'user28', 'purchases': ['croma', 'vijaysales', 'flipkart']},
        {'user': 'user29', 'purchases': ['uber', 'ola', 'blinkit']},
        {'user': 'user30', 'purchases': ['swiggy', 'dominos']},
        {'user': 'user31', 'purchases': ['amazon', 'myntra', 'nykaa', 'wildcraft', 'mcd']},
        {'user': 'user32', 'purchases': ['puma', 'maxfashion', 'croma']},
        {'user': 'user33', 'purchases': ['vijaysales', 'amazon', 'reliancesmart']},
        {'user': 'user34', 'purchases': ['pvr', 'zee5']},
        {'user': 'user35', 'purchases': ['ola', 'uber', 'blinkit', 'pizzahut']},
        {'user': 'user36', 'purchases': ['flipkart', 'myntra', 'nykaa']},
        {'user': 'user37', 'purchases': ['maxfashion', 'puma']},
        {'user': 'user38', 'purchases': ['dominos', 'kfc', 'mcd', 'swiggy']},
        {'user': 'user39', 'purchases': ['croma', 'vijaysales', 'reliancesmart']},
        {'user': 'user40', 'purchases': ['zee5', 'pvr', 'prime']},
        {'user': 'user41', 'purchases': ['amazon', 'flipkart', 'myntra', 'maxfashion']},
        {'user': 'user42', 'purchases': ['amazon', 'flipkart', 'pvr']},
        {'user': 'user43', 'purchases': ['dominos', 'kfc', 'swiggy']},
        {'user': 'user44', 'purchases': ['myntra', 'nykaa', 'croma']},
        {'user': 'user45', 'purchases': ['mcd', 'kfc', 'pizzahut']},
        {'user': 'user46', 'purchases': ['zee5', 'pvr', 'prime', 'reliancesmart']},
        {'user': 'user47', 'purchases': ['nykaa', 'wildcraft', 'flipkart']},
        {'user': 'user48', 'purchases': ['croma', 'vijaysales', 'reliancesmart']},
        {'user': 'user49', 'purchases': ['uber', 'ola', 'blinkit']},
        {'user': 'user50', 'purchases': ['swiggy', 'dominos', 'maxfashion']},
        {'user': 'user51', 'purchases': ['amazon', 'myntra', 'nykaa', 'wildcraft', 'mcd']},
        {'user': 'user52', 'purchases': ['puma', 'maxfashion', 'croma']},
        {'user': 'user53', 'purchases': ['vijaysales', 'amazon', 'reliancesmart']},
        {'user': 'user54', 'purchases': ['pvr', 'zee5']},
        {'user': 'user55', 'purchases': ['ola', 'uber', 'blinkit', 'pizzahut']},
        {'user': 'user56', 'purchases': ['flipkart', 'myntra', 'nykaa']},
        {'user': 'user57', 'purchases': ['maxfashion', 'puma', 'swiggy']},
        {'user': 'user58', 'purchases': ['dominos', 'kfc', 'mcd', 'swiggy']},
        {'user': 'user59', 'purchases': ['croma', 'vijaysales', 'reliancesmart']},
        {'user': 'user60', 'purchases': ['zee5', 'pvr', 'prime']},
        {'user': 'user61', 'purchases': ['amazon', 'flipkart', 'myntra']},
        {'user': 'user62', 'purchases': ['amazon', 'flipkart']},
        {'user': 'user63', 'purchases': ['dominos', 'kfc', 'swiggy']},
        {'user': 'user64', 'purchases': ['myntra', 'nykaa', 'pvr', 'maxfashion']},
        {'user': 'user65', 'purchases': ['mcd', 'kfc', 'pizzahut']},
        {'user': 'user66', 'purchases': ['zee5', 'pvr', 'prime', 'reliancesmart']},
        {'user': 'user67', 'purchases': ['nykaa', 'wildcraft']},
        {'user': 'user68', 'purchases': ['croma', 'vijaysales', 'flipkart']},
        {'user': 'user69', 'purchases': ['uber', 'ola', 'blinkit']},
        {'user': 'user70', 'purchases': ['swiggy', 'dominos']},
        {'user': 'user71', 'purchases': ['amazon', 'myntra', 'nykaa', 'wildcraft', 'mcd']},
        {'user': 'user72', 'purchases': ['puma', 'maxfashion', 'croma']},
        {'user': 'user73', 'purchases': ['vijaysales', 'amazon', 'reliancesmart']},
        {'user': 'user74', 'purchases': ['pvr', 'zee5']},
        {'user': 'user75', 'purchases': ['ola', 'uber', 'blinkit', 'pizzahut']},
        {'user': 'user76', 'purchases': ['flipkart', 'myntra', 'nykaa']},
        {'user': 'user77', 'purchases': ['maxfashion', 'puma']}]

    # Convert provided data to DataFrame
    df1 = pd.DataFrame(data)

    # Load additional dataset
    df2 = pd.read_csv('../recommendation.csv')
    df2 = df2.rename(columns={'userid': 'user', 'item': 'purchases'})
    df2 = df2[['user', 'purchases']]

    # Merge datasets
    df = pd.concat([df1, df2], ignore_index=True)
    # df = df1
    print(df.head())

    df_exploded = df.explode('purchases')

    # Example item types dictionary
    item_types = {
        'amazon': 'e-commerce',
        'flipkart': 'e-commerce',
        'myntra': 'fashion',
        'mcd': 'food',
        'dominos': 'food',
        'kfc': 'food',
        'swiggy': 'food',
        'maxfashion': 'fashion',
        'nykaa': 'fashion',
        'pvr': 'entertainment',
        'pizzahut': 'food',
        'zee5': 'entertainment',
        'prime': 'entertainment',
        'reliancesmart': 'retail',
        'wildcraft': 'fashion',
        'blinkit':'delivery',
        'swiggy':'delivery',
        'uber':'cab',
        'ola':'cab',
        'croma':'retail',
        'vijaysales':'retail'
        # Add more items as needed
    }

    # Assign item types to each purchase
    df_exploded['item_type'] = df_exploded['purchases'].map(item_types)
    print(df_exploded.head())

    return df_exploded