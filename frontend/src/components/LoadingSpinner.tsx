import styles from "../styles/LoadingSpinner.module.css";

export const LoadingSpinner = () => {
    return (
        <div className={styles.ldsRipple}>
            <div></div>
            <div></div>
        </div>
    );
};
