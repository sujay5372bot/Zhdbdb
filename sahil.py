�
    [C�f�  �                   �n  � d dl Z d dlZd dlZd dlmZ d dlmZ d dlmZ  ed�  �          ed�  �          eddd�  �        Z	d	� Z
 e
�   �           ej        ej        d
��  �          edd�  �        5 Zd� eD �   �         Zddd�  �         n# 1 swxY w Y   d� Zdd�Zd� Zd� Zedk    r e�   �          dS dS )�    N)�RequestException)�Thread)�datetime�$This File Is Made By @SahilModzOwneri�  �	   �   c                  �   � t          j        �   �         } | t          k    rt          d�  �         t	          �   �          d S d S )Nz:THE FILE IS CLOSED. DM TO BUY PAID FILE :- @SAHILMODZOWNER)r   �now�expiry_date�print�exit)�current_dates    �sahil.py�check_expiryr      s<   � ��<�>�>�L��k�!�!��J�K�K�K������� "�!�    z%(asctime)s - %(message)s)�level�formatz
tokens.txt�rc                 �^   � g | ]*}|�                     �   �         �|�                     �   �         ��+S � )�strip)�.0�lines     r   �
<listcomp>r      s-   � �<�<�<�t�t�z�z�|�|�<�d�j�j�l�l�<�<�<r   c                 �B  � t          j        d| � d��  �         d| � d�}	 t          j        ||��  �        }|�                    �   �          |j        dv rt          j        d| � d��  �         d	S n1# t          $ r$}t          j        d
| � d|� ��  �         Y d }~nd }~ww xY wdS )NzStarting Codespace: z...�'https://api.github.com/user/codespaces/z/start��headers)��   ��   �
Codespace z is starting.TzError starting Codespace �: F)�logging�info�requests�post�raise_for_status�status_coder   �error)�codespace_namer   �	start_url�start_response�es        r   �start_codespacer.   !   s�   � ��L�;��;�;�;�<�<�<�P�.�P�P�P�I�I�!��y�'�B�B�B���'�'�)�)�)��%��3�3��L�C�n�C�C�C�D�D�D��4� 4�� � I� I� I���G�.�G�G�A�G�G�H�H�H�H�H�H�H�H�����I�����5s   �AA. �.
B�8B�B�   c                 �,  � t          j        d| � d��  �         	 	 t          j        d| � �|��  �        }|�                    �   �          |�                    �   �         �                    d�  �        }t          j        d| � d|� ��  �         |d	k    r)t          j        d| � d
��  �         t          | |�  �         nt          j        d| � ��  �         n1# t          $ r$}t          j        d| � d|� ��  �         Y d }~nd }~ww xY wt          j
        |�  �         ��)NzKeeping Codespace z	 alive...Tr   r   �stater!   z state: �Shutdownz' is shut down. Attempting to restart...z&Successfully pinged Codespace API for z Error pinging Codespace API for r"   )r#   r$   r%   �getr'   �jsonr.   r   r)   �time�sleep)r*   r   �interval�responser1   r-   s         r   �
keep_aliver9   /   sQ  � ��L�?�n�?�?�?�@�@�@��	T��|�$^�n�$^�$^�ho�p�p�p�H��%�%�'�'�'��M�M�O�O�'�'��0�0�E��L�E�n�E�E�e�E�E�F�F�F��
�"�"���a�.�a�a�a�b�b�b����8�8�8�8���V�n�V�V�W�W�W���� 	T� 	T� 	T��M�R�^�R�R�q�R�R�S�S�S�S�S�S�S�S�����	T�����
�8����s   �B4C �
C>�C9�9C>c                 �P  � d| � �dd�}	 t          j        d|��  �        }|�                    �   �          |�                    �   �         d         }|r�g }|D ]s}|d         }t	          j        d|� d	��  �         t          ||�  �         t          t          ||f�
�  �        }|�	                    �   �          |�
                    |�  �         �t|D ]}|�                    �   �          �d S t	          j        d�  �         d S # t          $ r"}t	          j        d|� ��  �         Y d }~d S d }~ww xY w)Nztoken zapplication/vnd.github.v3+json)�Authorization�Acceptz&https://api.github.com/user/codespacesr   �
codespaces�namezFound Codespace: z for token.��target�argsz#No Codespaces found for this token.z'Error retrieving Codespaces for token: )r%   r3   r'   r4   r#   r$   r.   r   r9   �start�append�joinr   r)   )	�tokenr   r8   r=   �threads�	codespacer*   �threadr-   s	            r   �handle_codespaces_for_tokenrI   A   s{  � �)�%�)�)�2�� �G�E��<� H�RY�Z�Z�Z���!�!�#�#�#��]�]�_�_�\�2�
�� 	@��G�'� '� '�	�!*�6�!2����L��L�L�L�M�M�M����8�8�8�  �z���8Q�R�R�R�����������v�&�&�&�&� "� � ���������� � �L�>�?�?�?�?�?��� E� E� E���C��C�C�D�D�D�D�D�D�D�D�D�����E���s   �CC9 �#C9 �9
D%�D � D%c                  ��   � t          d�  �         g } t          D ]B}t          t          |f��  �        }|�                    �   �          | �                    |�  �         �C| D ]}|�                    �   �          �d S )Nr   r?   )r   �tokensr   rI   rB   rC   rD   )rF   rE   rH   s      r   �mainrL   `   s�   � �	�
0�1�1�1��G�� � ���:�%��J�J�J�����������v����� � � ���������� r   �__main__)r/   )r5   r%   r#   �requests.exceptionsr   �	threadingr   r   r   r   r   �basicConfig�INFO�open�filerK   r.   r9   rI   rL   �__name__r   r   r   �<module>rU      s�  �� ���� ���� ���� 0� 0� 0� 0� 0� 0� � � � � � � � � � � � � ��,� -� -� -� ��,� -� -� -� �h�t�Q��#�#��� � � ����� �� �'�,�/J� K� K� K� K� 
�T�,���� =��<�<�t�<�<�<�F�=� =� =� =� =� =� =� =� =� =� =���� =� =� =� =�� � �� � � �$E� E� E�>� � � �z����D�F�F�F�F�F� �s   �2B�B�B